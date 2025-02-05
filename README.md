# Python x Yaml CV GEn :)

Un générateur de CV professionnel utilisant Flask et WeasyPrint pour créer des CV élégants au format HTML et PDF à partir de données YAML.

## 🌟 Fonctionnalités

- Interface web responsive
- Export PDF professionnel
- Design moderne avec sidebar
- Support des emojis
- Mise en page optimisée pour le format A4
- Personnalisation du contenu du CV via fichier YAML
- Support du HTML dans les textes

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip
- WeasyPrint (nécessite des dépendances système)
- Flask

### Installation des dépendances système (pour WeasyPrint)

#### Debian/Ubuntu
```bash
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

#### MacOS
```bash
brew install cairo pango gdk-pixbuf libffi
```

### Installation du projet

1. Cloner le dépôt :
```bash
git clone [URL_DU_REPO]
cd python-x-yaml-cv-generator
```

2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ou
.\venv\Scripts\activate  # Windows
```

3. Installer les dépendances Python :
```bash
pip install -r requirements.txt
```

## 📝 Configuration

1. Créer votre fichier CV en YAML (cf cv_sample.yaml pour la structure complète) :
```yaml
cv:
  resume:
    summary: "Votre résumé professionnel"
  experiences:
    - period: "2025 - Aujourd'hui"
      company: "Entreprise"
      title: "Poste"
      responsibilities:
        - "Description du poste"
```

2. Ajouter votre photo de profil :
   - Placez votre photo au format JPG dans le dossier du projet
   - Nommez-la `photo.jpg`

## 🖥️ Utilisation

1. Lancer l'application :
```bash
python app.py
```

2. Accéder à l'interface :
   - Ouvrir `http://localhost:5000` dans votre navigateur
   - Visualiser votre CV en HTML
   - Utiliser le bouton "Télécharger en PDF" pour obtenir la version PDF

## 🛠️ Structure du projet

```
cv-generator/
├── app.py               # Application Flask
├── cv_sample.yaml       # Données du CV
├── photo_sample.jpg     # Photo de profil
├── requirements.txt     # Dépendances Python
└── templates/
    └── cv_template.html # Template du CV
```

## 📋 Format YAML

Le fichier YAML accepte les balises HTML dans les champs texte :
```yaml
title: "<strong>Développeur Full Stack</strong>"
```

## ⚙️ Personnalisation

### Modification du style
- Le template utilise des variables CSS pour les couleurs
- Les dimensions sont optimisées pour le format A4
- La mise en page est contrôlée par CSS Grid

### Ajout d'emojis
- Les emojis sont supportés dans tous les champs texte
- Utilisez-les pour les titres de sections ou les compétences

## 📄 Licence

MIT License - voir le fichier [LICENSE](https://github.com/popallo/python-x-cv-generator?tab=MIT-1-ov-file) pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commit vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou à me contacter.