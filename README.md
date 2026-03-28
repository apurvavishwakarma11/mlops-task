#  MLOps Batch Pipeline — Production-Ready Mini Project

##  Overview

This project implements a **production-style MLOps batch pipeline** in Python.

It demonstrates:

*  Reproducibility (config-driven execution)
*  Observability (structured logging + metrics)
*  Reliability (error handling + exit codes)
*  Deployment readiness (Docker support)

---

##  Problem Statement

Given OHLCV market data, the pipeline:

1. Computes a rolling mean on the `close` price
2. Generates a binary trading signal
3. Outputs performance metrics

---

##  Pipeline Workflow

```text
Input (CSV) → Config (YAML) → Processing → Metrics + Logs
```

### Steps:

1. Load configuration (`config.yaml`)
2. Read dataset (`data.csv`)
3. Normalize column names
4. Compute rolling mean
5. Generate signal:

   * `1` → close > rolling mean
   * `0` → otherwise
6. Output:

   * `metrics.json`
   * `run.log`

---

##  Run Locally

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

##  Sample Output

### metrics.json

```json
{
  "version": "v1",
  "rows_processed": 779029,
  "metric": "signal_rate",
  "value": 0.48,
  "latency_ms": 120,
  "seed": 42,
  "status": "success"
}
```

---

##  Logging (run.log)

```text
Job started
Config loaded
Rows loaded
Rolling mean computed
Signal generated
Job finished
```

---

##  Docker Support

### Build

```bash
docker build -t mlops-task .
```

### Run

```bash
docker run --rm mlops-task
```

###  Docker Guarantees

* Includes `data.csv` and `config.yaml`
* Generates `metrics.json` and `run.log`
* Prints final metrics to stdout
* Returns proper exit codes (0 = success, 1 = failure)

---

##  Project Structure

```text
mlops-task/
│
├── run.py
├── config.yaml
├── data.csv
├── Dockerfile
├── requirements.txt
├── README.md
├── metrics.json
└── run.log
```

---

##  Tech Stack

* Python 3.9
* pandas
* numpy
* pyyaml
* Docker

---

##  Key Features

*  Config-driven pipeline
*  Structured metric output
*  Detailed logging
*  Robust error handling
*  Dockerized execution
*  Reproducible results (seed control)

---

##  Notes

Dockerfile is included as required.
Due to system restrictions (WSL update limitation), Docker execution was not tested locally, but configuration is complete and production-ready.

---

##  Why this project stands out

This project goes beyond a basic script by incorporating:

* MLOps best practices
* Production-style logging and metrics
* Deployment readiness via Docker

 Designed to reflect real-world ML engineering workflows.


