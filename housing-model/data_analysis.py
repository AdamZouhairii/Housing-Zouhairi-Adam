import pandas as pd

# Charger les données
data = pd.read_csv("housing.csv")

# Aperçu des données
print(data.head())
print(data.info())

# Vérifier les valeurs manquantes
print(data.isnull().sum())

# Remplir les valeurs manquantes
data['total_bedrooms'].fillna(data['total_bedrooms'].median(), inplace=True)

# Vérifier les statistiques descriptives
print(data.describe())

# Exporter les données nettoyées
data.to_csv("processed_housing.csv", index=False)
