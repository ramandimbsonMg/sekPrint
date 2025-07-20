from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.models import Etudiant
from classe.models import Classe
from school.models import Ecole


def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    return render(request, 'landing.page.html')


@login_required
def dashboard(request):
    ecoles = Ecole.objects.filter(user=request.user)
    classes = Classe.objects.filter(ecole__in=ecoles)
    etudiants = Etudiant.objects.filter(classe__in=classes)

    return render(request, "dashboard.html", {
        "etudiants_count": etudiants.count(),
        "ecoles_count": ecoles.count(),
        "classes_count": classes.count()
    })