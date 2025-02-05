from flask import Flask, render_template, send_file
import yaml
from weasyprint import HTML
import base64
from io import BytesIO

app = Flask(__name__)

def load_yaml_data(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def get_base64_photo(photo_path):
    with open(photo_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

@app.route('/')
def show_cv():
    """Affiche le CV en HTML"""
    cv_data = load_yaml_data('cv_sample.yaml')
    photo_base64 = get_base64_photo('photo_sample.jpg')
    
    return render_template(
        'cv_template.html',
        cv=cv_data['cv'],
        photo=photo_base64,
        show_download=False  # Pour afficher le bouton de téléchargement
    )

@app.route('/download-pdf')
def download_pdf():
    """Génère et télécharge le CV en PDF"""
    cv_data = load_yaml_data('cv_sample.yaml')
    photo_base64 = get_base64_photo('photo_sample.jpg')
    
    html_content = render_template(
        'cv_template.html',
        cv=cv_data['cv'],
        photo=photo_base64,
        show_download=False
    )
    
    # Convertir en PDF
    pdf = HTML(string=html_content).write_pdf()
    
    # Créer un BytesIO object
    pdf_buffer = BytesIO(pdf)
    pdf_buffer.seek(0)
    
    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='cv_sample.pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)