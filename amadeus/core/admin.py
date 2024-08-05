# admin.py
from django.contrib import admin
from .models import User  # Importez le modèle défini dans models.py

# Enregistrez le modèle User dans l'admin
admin.site.register(User)
