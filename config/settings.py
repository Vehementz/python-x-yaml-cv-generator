import os

# Chemins des dossiers
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
EXAMPLES_DIR = os.path.join(BASE_DIR, 'examples')

# Structure des dossiers de données
CV_DIR = os.path.join(DATA_DIR, 'cvs')
PHOTOS_DIR = os.path.join(DATA_DIR, 'photos')

# Création des dossiers nécessaires
os.makedirs(CV_DIR, exist_ok=True)
os.makedirs(PHOTOS_DIR, exist_ok=True)