# 🏫 SekPrint – Générateur de Badge pour Écoles

SekPrint est une application Django pour la gestion des écoles, des étudiants et la **génération automatique de badges PDF avec QR code**.

## 🎯 Objectif

Permettre à chaque école de :
- Gérer les inscriptions des étudiants
- Générer un badge personnalisé (nom,prenom,matricule, photo, QR code)
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
- qrcode (génération de QR codes)

## 📦 Installation

```bash
git clone https://github.com/ramandimbsonMg/sekprint.git
cd Sekprint
python -m venv env
source env/bin/activate  # ou .\env\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

👨‍💻 Auteur
Espoir Ramandimbson

Étudiant en informatique, Madagascar 🇲🇬

📧 ramandimbonespoir@gmail.com

💼 LinkedIn
www.linkedin.com/in/ramandimbson-espoir-mathieu-8a4516291

💼 Facebook
https://www.facebook.com/teresperant/

🪪 Licence
Ce projet est open-source sous licence MIT.
Vous pouvez le réutiliser et le modifier librement.

🌟 Notes
Ce projet est une base fonctionnelle pour la gestion et la création automatisée de badges d’écoles, facilement extensible pour d’autres fonctionnalités comme :

Gestion des utilisateurs et permissions avancées

Historique des badges générés

Notifications par email
