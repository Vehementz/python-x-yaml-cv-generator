FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances Python uniquement
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers nécessaires
COPY app.py .
COPY config/ ./config/
COPY templates/ ./templates/

# Création des dossiers pour les données
RUN mkdir -p data/cvs data/photos

CMD ["flask", "run", "--host=0.0.0.0"]