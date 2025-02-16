# Importation de la fonction path pour définir les routes
from django.urls import path
from . import views  # Importation des vues définies dans le fichier views.py

# Nom d'espace de l'application pour éviter les conflits de noms dans les URL
app_name = "accounts"

# Définition des URLs pour le module d'authentification
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup"),
    # URL pour l'inscription d'un nouvel utilisateur

    path('profile/', views.ProfileView.as_view(), name="profile"),
    # URL pour afficher le profil de l'utilisateur connecté

    path('modifier_profile/', views.ModifierProfileView.as_view(),
        name="modifier_profile"),
    # URL pour modifier le profil de l'utilisateur connecté

    path('login/', views.LoginViewCustom.as_view(), name='login'),
    # URL pour la page de connexion

    path('password_reset/', views.PasswordResetViewCustom.as_view(),
        name='password_reset'),
    # URL pour la page de réinitialisation de mot de passe
]
