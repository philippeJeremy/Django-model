from django.contrib import admin
from .models import User  # Importation du modèle User

# Enregistrement du modèle User dans l'interface d'administration Django


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage du modèle User dans l'admin Django.
    """
    list_display = ('nom', 'prenom', 'email', 'phone',
                    'is_active', 'is_staff', 'is_admin')
    # Liste des champs affichés dans l'interface d'administration
