from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from student.models import Etudiant
from classe.models import Classe
from school.models import Ecole


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

# Vue login
def user_login(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Modifier ici selon ta page d'accueil
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect."

    return render(request, "login.html", {"error": error})

# Vue register
def user_register(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            error = "Les mots de passe ne correspondent pas."
        elif User.objects.filter(username=username).exists():
            error = "Ce nom d'utilisateur est déjà pris."
        elif User.objects.filter(email=email).exists():
            error = "Cet email est déjà utilisé."
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            return redirect("creer_ecole")  # 🔁 Redirection après inscription

    return render(request, "register.html", {"error": error})
# Vue logout
def user_logout(request):
    logout(request)
    return redirect("login")
