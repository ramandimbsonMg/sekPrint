from django.db import models

from school.models import Ecole

# Create your models here.
class Classe(models.Model):
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)  # ✅ ce champ doit exister
    nom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.niveau} - {self.nom}"

