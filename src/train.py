from src.data_loader import load_transactions
from src.preprocessing import preprocess
from src.feature_engineering import create_features


def train_pipeline():

    print("Carregando dados...")

    df = load_transactions(
        "data/raw/transactions.csv"
    )

    print("Pré-processando...")

    df = preprocess(df)

    print("Criando atributos...")

    df = create_features(df)

    print(df.head())

    print()

    print("Pipeline executado com sucesso.")
