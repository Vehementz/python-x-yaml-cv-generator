# Python x Yaml CV GEn 📄

Un générateur de CV professionnel utilisant Flask et WeasyPrint pour créer des CV élégants au format HTML et PDF à partir de données YAML.

## 🌟 Fonctionnalités

- Interface web responsive
- Export PDF professionnel
- Design moderne avec sidebar
- Support des emojis
- Mise en page optimisée pour le format A4
- Personnalisation via fichier YAML
- Support du HTML dans les textes
- Conteneurisation Docker

## 🚀 Installation

### Option 1 : Avec Docker (recommandé)

1. Cloner le dépôt :
```bash
git clone [URL_DU_REPO]
cd cv-generator
```

2. Construire et lancer avec Docker Compose :
```bash
docker-compose up -d --build
```

Ou avec Docker directement :
```bash
# Construire l'image
docker build -t cv-generator .

# Lancer le conteneur
docker run -d -p 5000:5000 -v $(pwd)/cv_sample.yaml:/app/cv_sample.yaml:ro --name cv-generator cv-generator
```

### Option 2 : Installation locale

#### Prérequis

- Python 3.8 ou supérieur
- pip
- WeasyPrint (nécessite des dépendances système)

#### Dépendances système (pour WeasyPrint)

Pour Debian/Ubuntu :
```bash
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

Pour MacOS :
```bash
brew install cairo pango gdk-pixbuf libffi
```

#### Installation du projet

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ou
.\venv\Scripts\activate  # Windows
```

2. Installer les dépendances Python :
```bash
pip install -r requirements.txt
```

## 📝 Configuration

1. Créer votre fichier CV en YAML :
```yaml
cv:
  resume:
    summary: "Votre résumé professionnel"
  experiences:
    - period: "2023 - Aujourd'hui"
      company: "Entreprise"
      title: "Poste"
      responsibilities:
        - "Description du poste"
```

2. Ajouter votre photo de profil :
   - Placez votre photo au format JPG dans le dossier du projet
   - Nommez-la `photo_sample.jpg`

## 🖥️ Utilisation

1. Accéder à l'interface :
   - Ouvrir `http://localhost:5000` dans votre navigateur
   - Visualiser votre CV en HTML
   - Utiliser le bouton "Télécharger en PDF" pour obtenir la version PDF

## 🛠️ Structure du projet

```
cv-generator/
├── app.py               # Application Flask
├── cv_sample.yaml       # Exemple de CV
├── photo_sample.jpg     # Photo de profil
├── requirements.txt     # Dépendances Python
├── Dockerfile           # Configuration Docker
├── docker-compose.yml   # Configuration Docker Compose
└── templates/
    └── cv_template.html # Template du CV
```

## 📋 Format YAML

Le fichier YAML supporte les balises HTML :
```yaml
title: "<strong>Développeur Full Stack</strong>"
```

### Exemple Complet
Voir le fichier `cv_sample.yaml` pour un exemple complet de structure.

## ⚙️ Personnalisation

### Modification du style
- Le template utilise des variables CSS pour les couleurs
- Les dimensions sont optimisées pour le format A4
- La mise en page est contrôlée par CSS Grid

### Ajout d'emojis
- Les emojis sont supportés dans tous les champs texte
- Utilisez-les pour les titres de sections ou les compétences

## 🐳 Docker

### Variables d'environnement
- `FLASK_APP`: Nom de l'application Flask (défaut: app.py)
- `FLASK_ENV`: Environnement Flask (défaut: production)

### Volumes
Le fichier `cv_sample.yaml` est monté en lecture seule dans le conteneur.

### Ports
Le port 5000 est exposé et peut être mappé selon vos besoins.

## 📄 Licence

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commit vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue.