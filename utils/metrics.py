import json


def write_success_metrics(output_file, version, rows_processed,
                          signal_rate, latency_ms, seed):

    metrics = {
        "version": version,
        "rows_processed": rows_processed,
        "metric": "signal_rate",
        "value": round(signal_rate, 4),
        "latency_ms": round(latency_ms),
        "seed": seed,
        "status": "success"
    }

    with open(output_file, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


def write_error_metrics(output_file, version, error_message):

    metrics = {
        "version": version,
        "status": "error",
        "error_message": error_message
    }

    with open(output_file, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics