# src/train.py
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    # 1. Carregar dados processados
    data_path = os.path.join("data", "processed", "data_cleaned.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError("Arquivo de dados processados não encontrado.")
        
    df = pd.read_csv(data_path)
    
    # 2. Separar Features (X) e Target (y)
    X = df.drop(columns=["target"])
    y = df["target"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 3. Treinar o Modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Avaliar o Modelo
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Acurácia do Modelo: {acc * 100:.2f}%")
    print("\nRelatório de Classificação:\n", classification_report(y_test, predictions))
    
    # 5. Salvar o Modelo Treinado
    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "model.pkl")
    joblib.dump(model, model_path)
    print(f"Modelo salvo com sucesso em: {model_path}")

if __name__ == "__main__":
    train_model()
