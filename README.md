# SekPrint – Générateur de Badge pour Écoles

SekPrint est une application Django pour la gestion des écoles, des étudiants et la **génération automatique de badges PDF avec QR code**.

## 🎯 Objectif

Permettre à chaque école de :
- Gérer les inscriptions des étudiants
- Générer un badge personnalisé (nom, photo, QR code)
- Choisir la couleur du badge
- Télécharger le badge en PDF

## 🚀 Fonctionnalités

- 🔐 Authentification sécurisée
- 🏫 Gestion des écoles et des classes
- 👩‍🎓 Gestion des étudiants
- 🎟️ Génération de badges PDF avec QR Code
- 🎨 Personnalisation des badges (couleur)
- 📥 Export des badges en PDF

## ⚙️ Technologies

- Django 4.x
- PostgreSQL ou SQLite
- Tailwind CSS
- WeasyPrint ou ReportLab (pour PDF)
- qrcode (génération de QR codes)

## 📦 Installation

```bash
git clone https://github.com/ton-compte/sekprint.git
cd sekprint
python -m venv env
source env/bin/activate  # ou .\env\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
