from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from school.models import Ecole
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def creer_ecole(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        adresse = request.POST.get("adresse")
        logo = request.FILES.get("logo")

        # 🔐 L’école est liée à l’utilisateur connecté
        Ecole.objects.create(
            user=request.user,
            nom=nom,
            adresse=adresse,
            logo=logo
        )
        return redirect("dashboard") 
    ecoles = Ecole.objects.all()

    return render(request, "school.view.html", {"ecoles": ecoles})
    
def delete_ecole(request, id):
    ecole = get_object_or_404(Ecole, id=id)
    if request.method == "POST":
        ecole.delete()
        return redirect('add_ecole')
    return HttpResponse(status=405)