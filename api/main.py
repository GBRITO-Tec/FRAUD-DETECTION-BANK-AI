# api/main.py
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Data Science & ML API",
    description="API para disponibilizar predições do modelo treinado.",
    version="1.0.0"
)

# Carregar o modelo
try:
    model = joblib.load("models/model.pkl")
except Exception:
    model = None

class PredictionInput(BaseModel):
    features: list[float]

@app.get("/")
def read_root():
    return {"message": "API operacional. Acesse /docs para ver a documentação interativa."}

@app.post("/predict")
def predict(data: PredictionInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo não encontrado. Treine o modelo primeiro.")
    
    features_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features_array)
    return {"prediction": int(prediction[0])}
