FROM python:3.11-slim

# Installer les dépendances
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 8001

# Commande pour démarrer l'API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
