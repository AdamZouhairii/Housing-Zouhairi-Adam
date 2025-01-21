#!/bin/bash

set -e  # Arrêter le script en cas d'erreur

# Couleurs pour les logs
GREEN='\033[0;32m'
NC='\033[0m' # Pas de couleur

echo -e "${GREEN}--- Lancement des migrations avec Alembic ---${NC}"
alembic upgrade head

echo -e "${GREEN}--- Démarrage de l'application FastAPI ---${NC}"
poetry run python app/main.py
