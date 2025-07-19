from django.contrib import messages
from django.shortcuts import redirect, render
from badge.views import generate_and_save_qrcode
from .models import Classe, Ecole, Etudiant
# Create your views here.


def add_etudiant(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        ecole = Ecole.objects.get(id=data['ecole'])
        classe = Classe.objects.get(id=data['classe']) if data.get('classe') else None

        # Vérifier unicité matricule avant création
        if Etudiant.objects.filter(matricule=data['matricule']).exists():
            messages.error(request, "Le matricule existe déjà. Veuillez en choisir un autre.")
            # Recharger la page avec le message d’erreur
        else:
            etudiant = Etudiant.objects.create(
                nom=data['nom'],
                prenom=data['prenom'],
                matricule=data['matricule'],
                date_naissance=data['date_naissance'],
                photo=files.get('photo'),  # get pour éviter crash si pas envoyé
                ecole=ecole,
                classe=classe,
            )
            generate_and_save_qrcode(etudiant)  # Génération QR code
            messages.success(request, f"Étudiant {etudiant.prenom} ajouté avec succès.")
            return redirect('add_etudiant')

    ecoles = Ecole.objects.all()
    classes = Classe.objects.all()
    etudiants = Etudiant.objects.all().order_by('-id')  # derniers en premier

    return render(request, "student.view.html", {
        "ecoles": ecoles,
        "classes": classes,
        "etudiants": etudiants,
    })