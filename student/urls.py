from django.urls import path
from .views import add_etudiant

urlpatterns = [
    path("badge/add/", add_etudiant, name="add_etudiant"),
]
