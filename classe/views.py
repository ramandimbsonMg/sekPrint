from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from school.models import Ecole
from django.contrib.auth.decorators import login_required
from classe.models import Classe

# Create your views here.
@login_required
def add_classe(request):
    try:
        ecole = Ecole.objects.get(user=request.user)
    except Ecole.DoesNotExist:
        return render(request, "classe.view.html", {
            "error": "Aucune école associée à votre compte."
        })

    if request.method == "POST":
        nom = request.POST.get("nom")
        niveau = request.POST.get("niveau")
        Classe.objects.create(ecole=ecole, nom=nom, niveau=niveau)
        return redirect('add_classe')

    classes = Classe.objects.filter(ecole=ecole)
    return render(request, "classe.view.html", {"classes": classes})

def delete_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    if request.method == "POST":
        classe.delete()
        return redirect('add_classe')
    return HttpResponse(status=405)