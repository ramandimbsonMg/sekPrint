# Create your views here.
from django.contrib import messages
import base64
from django.shortcuts import redirect, render, get_object_or_404
from student.models import Etudiant
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def badge_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    return render(request, "badge.html", {"etudiant": etudiant})


def encode_image_to_base64(fieldfile):
    """
    Encode une image FileField en base64, ou retourne None si vide.
    """
    if not fieldfile:
        return None
    try:
        with fieldfile.open('rb') as f:
            data = f.read()
        return base64.b64encode(data).decode('utf-8')
    except Exception:
        return None

# Fonction d'analyse d'image (simple version simulée)
def detect_image_content(base64_image):
    # À remplacer par appel réel à une API IA (voir commentaire en bas)
    return {
        "type": "human",      # ou "anime", "object", "unknown"
        "gender": "female",   # si humain
        "character": None     # si anime
    }

def generate_pdf_badge(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    photo_base64 = encode_image_to_base64(etudiant.photo)
    logo_base64 = encode_image_to_base64(etudiant.ecole.logo) if etudiant.ecole.logo else None
    qrcode_base64 = encode_image_to_base64(etudiant.qrcode) if etudiant.qrcode else None

    # Analyse IA de la photo
    image_info = detect_image_content(photo_base64)

    # Render HTML
    template = get_template("components/badge.pdf.html")
    html = template.render({
        "etudiant": etudiant,
        "photo_base64": photo_base64,
        "logo_base64": logo_base64,
        "qrcode_base64": qrcode_base64,
        "image_info": image_info,
    })

    return HttpResponse(html)

def generate_and_save_qrcode(etudiant):
    data = f"Matricule: {etudiant.matricule}\nNom: {etudiant.prenom} {etudiant.nom}\nÉcole: {etudiant.ecole.nom}"
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    filename = f"qr_{etudiant.matricule}.png"
    filecontent = ContentFile(buffer.getvalue(), name=filename)
    etudiant.qrcode.save(filename, filecontent)
    etudiant.save()
