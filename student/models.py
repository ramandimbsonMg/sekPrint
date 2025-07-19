from django.db import models

from classe.models import Classe
from school.models import Ecole

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=30, unique=True)
    date_naissance = models.DateField()
    photo = models.ImageField(upload_to='etudiants/')
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True, blank=True)
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"