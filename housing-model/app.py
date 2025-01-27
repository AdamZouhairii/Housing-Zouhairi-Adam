from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Charger le modèle
model = joblib.load("housing_model.pkl")

# Initialiser l'application FastAPI
app = FastAPI()

# Définir le schéma pour les prédictions
class HousingData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    ocean_proximity: str

@app.post("/predict")
def predict(data: HousingData):
    # Convertir les données d'entrée en DataFrame
    input_data = pd.DataFrame([data.dict()])
    input_data = pd.get_dummies(input_data)

    # Prédire
    prediction = model.predict(input_data)
    return {"median_house_value": prediction[0]}
