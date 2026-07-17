import pandas as pd


def process_data(df, window):
    """
    Compute rolling mean and binary signal.
    """

    df = df.copy()

    df["rolling_mean"] = df["close"].rolling(window=window).mean()

    # Exclude first window-1 rows
    df = df.dropna().reset_index(drop=True)

    df["signal"] = (
        df["close"] > df["rolling_mean"]
    ).astype(int)

    return df