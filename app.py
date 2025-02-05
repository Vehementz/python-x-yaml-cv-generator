from flask import Flask, render_template, send_file, request, abort
import yaml
from weasyprint import HTML
import base64
from io import BytesIO
import os
from config.settings import *

app = Flask(__name__)

def load_yaml_data(yaml_file):
    """Charge les données depuis un fichier YAML"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except Exception as e:
        app.logger.error(f"Erreur lors de la lecture du YAML: {str(e)}")
        return None

def get_base64_photo(photo_path):
    """Convertit une photo en base64"""
    try:
        with open(photo_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        app.logger.error(f"Erreur lors de la lecture de la photo: {str(e)}")
        return None

def get_available_cvs():
    """Liste tous les CVs disponibles"""
    cvs = {}
    
    # Ajouter les CVs personnalisés
    for file in os.listdir(CV_DIR):
        if file.endswith('.yaml'):
            cv_id = os.path.splitext(file)[0]
            cvs[cv_id] = f'CV - {cv_id}'
    
    return cvs

def get_cv_path(cv_id):
    """Récupère le chemin du fichier CV"""
    
    cv_path = os.path.join(CV_DIR, f'{cv_id}.yaml')
    if os.path.exists(cv_path):
        return cv_path
    return None

def get_photo_path(cv_id):
    """Récupère le chemin de la photo"""
    
    # Chercher dans plusieurs extensions
    for ext in ['.jpg', '.jpeg', '.png']:
        photo_path = os.path.join(PHOTOS_DIR, f'{cv_id}{ext}')
        if os.path.exists(photo_path):
            return photo_path

@app.route('/')
def index():
    """Page d'accueil avec liste des CVs"""
    cvs = get_available_cvs()
    return render_template('index.html', cvs=cvs)

@app.route('/cv/<cv_id>')
def show_cv(cv_id):
    """Affiche un CV spécifique"""
    cv_path = get_cv_path(cv_id)
    if not cv_path:
        abort(404)
    
    cv_data = load_yaml_data(cv_path)
    if not cv_data:
        abort(500)
        
    photo_path = get_photo_path(cv_id)
    photo_base64 = get_base64_photo(photo_path)
    if not photo_base64:
        abort(500)
    
    return render_template(
        'cv_template.html',
        cv=cv_data['cv'],
        cv_id=cv_id,  # On ajoute l'ID ici
        photo=photo_base64,
        show_download=True
    )

@app.route('/download-pdf/<cv_id>')
def download_pdf(cv_id):
    """Télécharge le CV en PDF"""
    cv_path = get_cv_path(cv_id)
    if not cv_path:
        abort(404)
    
    cv_data = load_yaml_data(cv_path)
    if not cv_data:
        abort(500)
        
    photo_path = get_photo_path(cv_id)
    photo_base64 = get_base64_photo(photo_path)
    if not photo_base64:
        abort(500)
    
    html_content = render_template(
        'cv_template.html',
        cv=cv_data['cv'],
        photo=photo_base64,
        show_download=False
    )
    
    pdf = HTML(string=html_content).write_pdf()
    pdf_buffer = BytesIO(pdf)
    pdf_buffer.seek(0)
    
    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'cv_{cv_id}.pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)