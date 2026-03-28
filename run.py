import argparse
import pandas as pd
import numpy as np
import yaml
import logging
import time
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log-file", required=True)
    args = parser.parse_args()

    logging.basicConfig(
        filename=args.log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    start_time = time.time()

    try:
        logging.info("Job started")

        # Load config
        with open(args.config, "r") as f:
            config = yaml.safe_load(f)

        seed = config.get("seed")
        window = config.get("window")
        version = config.get("version")

        if seed is None or window is None or version is None:
            raise ValueError("Invalid config file")

        np.random.seed(seed)
        logging.info(f"Config loaded: seed={seed}, window={window}, version={version}")

        # Load dataset
        df = pd.read_csv(args.input, header=None)

# split the single column into multiple columns
        df = df[0].str.split(",", expand=True)

# set correct column names
        df.columns = ["timestamp","open","high","low","close","volume_btc","volume_usd"]

# remove header row if duplicated
        df = df[1:].reset_index(drop=True)

# convert close to numeric
        df["close"] = pd.to_numeric(df["close"], errors="coerce")

        logging.info(f"Rows loaded: {len(df)}")

        # Rolling mean
        df["rolling_mean"] = df["close"].rolling(window=window).mean()
        logging.info("Rolling mean computed")

        # Signal generation
        df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)
        logging.info("Signal generated")

        # Metrics
        rows_processed = len(df)
        signal_rate = df["signal"].mean()
        latency_ms = int((time.time() - start_time) * 1000)

        result = {
            "version": version,
            "rows_processed": rows_processed,
            "metric": "signal_rate",
            "value": round(signal_rate, 4),
            "latency_ms": latency_ms,
            "seed": seed,
            "status": "success"
        }

        logging.info(f"Metrics: {result}")

    except Exception as e:
        result = {
            "version": "v1",
            "status": "error",
            "error_message": str(e)
        }
        logging.error(str(e))

    # Always write output
    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    # Print output
    print(json.dumps(result, indent=2))

    logging.info("Job finished")


if __name__ == "__main__":
    main()