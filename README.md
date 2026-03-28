Docker setup included as required.
Due to system restrictions (WSL update not permitted), Docker could not be executed locally.
However, the project is fully functional and ready to run using Docker in a supported environment.
# ML Engineering Task - MLOps Batch Pipeline

##  Overview
This project implements a minimal MLOps-style batch pipeline in Python.

It demonstrates:
- Reproducibility (via config + seed)
- Observability (logs + metrics)
- Deployment readiness (Docker support)


##  How it works

1. Loads configuration from YAML
2. Reads OHLCV dataset (data.csv)
3. Computes rolling mean on 'close'
4. Generates binary signal:
   - 1 → close > rolling mean
   - 0 → otherwise
5. Outputs metrics and logs

