import pandas as pd


def create_features(df: pd.DataFrame):

    df = df.copy()

    df["high_value"] = (
        df["amount"] > 1000
    ).astype(int)

    df["night_transaction"] = (
        (df["hour"] <= 5)
        | (df["hour"] >= 22)
    ).astype(int)

    return df
