# MLOps Technical Assessment

## Overview
This project validates configuration and CSV input, computes a rolling mean on the `close` column, generates binary trading signals, logs execution, and outputs metrics in JSON format.

## Project Structure

```
mlops-assessment/
├── run.py
├── config.yaml
├── requirements.txt
├── Dockerfile
├── README.md
├── data/
│   └── data.csv
└── utils/
    ├── __init__.py
    ├── config.py
    ├── data_loader.py
    ├── processing.py
    ├── logger.py
    └── metrics.py
```

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python run.py --input data/data.csv --config config.yaml --output metrics.json --log-file run.log
```

## Docker

```bash
docker build -t mlops-task .
docker run --rm mlops-task
```