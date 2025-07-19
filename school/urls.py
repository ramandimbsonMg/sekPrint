from django.urls import path
from .views import (
    creer_ecole, delete_ecole,
)

urlpatterns = [
    path("creer-ecole", creer_ecole, name="creer_ecole"),
    path("ecole/<int:id>/delete/", delete_ecole, name="delete_ecole"),
]
