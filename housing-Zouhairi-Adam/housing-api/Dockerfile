FROM python:3.11-slim

# Installer Poetry et Alembic
RUN pip install poetry alembic

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN poetry install --no-root

# Exposer le port pour l'application
EXPOSE 8000

# Commande d'entrée
CMD ["bash", "/app/run.sh"]
