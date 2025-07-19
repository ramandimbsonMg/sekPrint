from django.db import models
from django.contrib.auth.models import User

class Ecole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 🔥 Relation ajoutée
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.nom
