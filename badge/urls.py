from django.urls import path
from .views import badge_etudiant, generate_pdf_badge

urlpatterns = [
    path('badge/<int:id>/', badge_etudiant, name='badge_etudiant'),
    path('badge/<int:id>/pdf/', generate_pdf_badge, name='pdf_badge'),
]
