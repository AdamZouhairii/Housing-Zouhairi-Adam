# Housing API

## Description
Cette application **FastAPI** gère des informations sur des maisons. Elle est entièrement dockerisée et utilise une base de données **PostgreSQL** hébergée sur **Railway**.

---

## Prérequis
- **Docker** et **Docker Compose**
- Python (facultatif pour développement local)

---

## Installation et Déploiement

### 1. Clonez le projet
Clonez ce dépôt sur votre machine :
```bash
git clone <repository_url>
cd Housing-API-Cloud-main
```

---

### 2. Configurez les variables d'environnement
Créez un fichier `.env` dans le dossier `housing-api/` ou modifiez celui existant :
```dotenv
DATABASE_URL=postgresql://postgres:bSeEHAPtQHrzhmLjTPppeagYaLkDwasS@postgres.railway.internal:5432/railway
```

---

### 3. Démarrez l'application avec Docker
Utilisez Docker Compose pour construire et lancer les conteneurs :
```bash
docker-compose up --build
```

L'API sera disponible sur **http://localhost:8000**.

---

## Commandes utiles

### 1. Accéder au conteneur PostgreSQL
Si vous souhaitez vérifier directement la base de données :
```bash
docker exec -it housing-api-db psql -U postgres -d railway
```

---

### 2. Lister les tables dans la base de données
Une fois connecté au conteneur PostgreSQL :
```sql
\dt
```

---

### 3. Voir le contenu de la table `houses`
Pour afficher toutes les entrées dans la table :
```sql
SELECT * FROM houses;
```

---

### 4. Tester l'API

#### a. Endpoint `POST /houses`
Envoyez une requête pour ajouter une maison à la base de données :
```bash
curl -X POST "http://localhost:8000/houses" \
-H "Content-Type: application/json" \
-d '{
  "longitude": -122,
  "latitude": 23,
  "housing_median_age": 37.88,
  "total_rooms": 41,
  "total_bedrooms": 880,
  "population": 129,
  "households": 322,
  "median_income": 126,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}'
```

#### b. Réponse attendue
Si tout fonctionne correctement, vous recevrez une réponse similaire à ceci :
```json
{
  "id": 1,
  "longitude": -122.0,
  "latitude": 23.0,
  "housing_median_age": 37.88,
  "total_rooms": 41,
  "total_bedrooms": 880,
  "population": 129,
  "households": 322,
  "median_income": 126.0,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}
```

---

### 5. Gestion des migrations Alembic
Les migrations sont appliquées automatiquement lors du démarrage du conteneur.

Si vous devez générer ou appliquer des migrations manuellement :
1. Générer une migration :
   ```bash
   docker exec -it housing-api-app alembic revision --autogenerate -m "Migration description"
   ```
2. Appliquer les migrations :
   ```bash
   docker exec -it housing-api-app alembic upgrade head
   ```

---

## Fonctionnalités
- Ajouter des maisons (POST `/houses`).
- Voir toutes les maisons via PostgreSQL.

---

## Problèmes courants

### 1. Erreur 422 (Unprocessable Entity)
Cela signifie que les données envoyées ne correspondent pas au schéma attendu. Assurez-vous que les noms des champs et leurs types sont corrects.

### 2. Problème de connexion à la base de données
Vérifiez que l'URL de votre base de données est correcte dans le fichier `.env`.

---

## Auteur
Adam Zouhairi







