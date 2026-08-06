from pathlib import Path
import pandas as pd


REQUIRED_COLUMNS = [
    "transaction_id",
    "customer_id",
    "amount",
    "transaction_type",
    "merchant_category",
    "channel",
    "hour",
    "is_fraud"
]


def load_transactions(csv_path: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV contendo transações.
    """

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)

    missing = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing:
        raise ValueError(
            f"Colunas obrigatórias ausentes: {missing}"
        )

    return df
