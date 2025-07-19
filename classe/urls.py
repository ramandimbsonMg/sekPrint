from django.urls import path
from .views import (
    add_classe, delete_classe,
)

urlpatterns = [
    path("classe/add/", add_classe, name="add_classe"),
    path("classe/<int:id>/delete/", delete_classe, name="delete_classe"),
]
