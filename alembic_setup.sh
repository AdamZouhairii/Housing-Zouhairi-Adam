#!/bin/bash

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}--- Initialisation d'Alembic ---${NC}"

if ! [ -x "$(command -v alembic)" ]; then
  echo -e "${RED}Alembic n'est pas installé. Installation en cours...${NC}"
  pip install alembic
  echo -e "${GREEN}Alembic installé avec succès.${NC}"
else
  echo -e "${GREEN}Alembic est déjà installé.${NC}"
fi

if [ -f .env ]; then
  export $(cat .env | xargs)
  echo -e "${GREEN}Variables d'environnement chargées depuis .env${NC}"
else
  echo -e "${RED}Fichier .env introuvable.${NC}" >&2
  exit 1
fi

echo -e "${GREEN}1. Création d'une nouvelle migration...${NC}"
alembic revision --autogenerate -m "Initial migration"

echo -e "${GREEN}2. Application des migrations...${NC}"
alembic upgrade head

echo -e "${GREEN}--- Migration terminée avec succès ---${NC}"
