import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Charger les données
data = pd.read_csv("processed_housing.csv")

# Séparer les features et la cible
X = data.drop("median_house_value", axis=1)
y = data["median_house_value"]

# Convertir les variables catégoriques en numériques
X = pd.get_dummies(X)

# Séparer les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de forêt aléatoire
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Évaluer le modèle
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Sauvegarder le modèle
joblib.dump(model, "housing_model.pkl")
