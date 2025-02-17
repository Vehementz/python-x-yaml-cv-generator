FROM python:3.9-alpine

# Ajout d'un utilisateur non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Installation des dépendances Python uniquement
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers nécessaires
COPY app.py .
COPY config/ ./config/
COPY templates/ ./templates/

# Création des dossiers pour les données
RUN mkdir -p data/cvs data/photos && chown -R appuser:appgroup data

# Changer l'utilisateur
USER appuser

CMD ["flask", "run", "--host=0.0.0.0"]