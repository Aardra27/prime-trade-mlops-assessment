import os
from io import StringIO

import pandas as pd


def load_data(file_path):
    """
    Load and validate dataset.
    Supports both normal CSVs and quoted malformed CSVs.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if os.path.getsize(file_path) == 0:
        raise ValueError("Input CSV is empty.")

    try:
        df = pd.read_csv(file_path)

        # Handle malformed CSVs that load into one column
        if len(df.columns) == 1:
            raise ValueError

    except Exception:

        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip().strip('"') for line in f]

        csv_text = "\n".join(lines)

        df = pd.read_csv(StringIO(csv_text))

    if "close" not in df.columns:
        raise ValueError("Missing required column: close")

    # Convert close column to numeric
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=["close"])

    return df