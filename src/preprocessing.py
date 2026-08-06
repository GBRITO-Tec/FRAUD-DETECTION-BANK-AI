import pandas as pd


def preprocess(df: pd.DataFrame):

    df = df.copy()

    df = df.drop_duplicates()

    df["amount"] = df["amount"].fillna(
        df["amount"].median()
    )

    df["merchant_category"] = (
        df["merchant_category"]
        .fillna("UNKNOWN")
    )

    df["channel"] = (
        df["channel"]
        .fillna("UNKNOWN")
    )

    return df
