from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Gestionnaire personnalisé pour le modèle User


class UserManager(BaseUserManager):
    """
    Classe de gestion des utilisateurs avec des méthodes pour créer un utilisateur normal,
    un utilisateur staff et un super-utilisateur.
    """

    def create_user(self, email, pseudo, nom, prenom, phone, password=None):
        """
        Crée et retourne un utilisateur avec l'email, pseudo, nom, prénom, téléphone et mot de passe.
        """
        if not email:
            raise ValueError(
                "Les utilisateurs doivent avoir une adresse e-mail")

        user = self.model(
            email=self.normalize_email(email),  # Normalisation de l'email
            pseudo=pseudo,
            nom=nom,
            prenom=prenom,
            phone=phone
        )
        user.set_password(password)  # Hachage du mot de passe
        user.save(using=self._db)  # Sauvegarde dans la base de données
        return user

    def create_staffuser(self, email, pseudo, nom, prenom, phone, password=None):
        """
        Crée et retourne un utilisateur staff (employé).
        """
        user = self.create_user(
            email=email,
            pseudo=pseudo,
            nom=nom,
            prenom=prenom,
            phone=phone,
            password=password
        )
        user.is_staff = True  # Définit l'utilisateur comme staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email, pseudo, nom, prenom, phone, password=None):
        """
        Crée et retourne un super-utilisateur avec tous les privilèges.
        """
        user = self.create_user(
            email=email,
            pseudo=pseudo,
            nom=nom,
            prenom=prenom,
            phone=phone,
            password=password
        )
        user.is_staff = True
        user.is_admin = True  # Donne le statut d'administrateur
        user.save(using=self._db)
        return user


# Modèle personnalisé d'utilisateur
class User(AbstractBaseUser, PermissionsMixin):
    """
    Modèle personnalisé pour remplacer l'utilisateur par défaut de Django.
    Utilise l'email comme identifiant principal au lieu du nom d'utilisateur.
    """

    pseudo = models.CharField(
        unique=True, max_length=30, blank=False, null=False)  # Pseudo unique
    nom = models.CharField(max_length=30, blank=False,
                            null=False)  # Nom de famille
    prenom = models.CharField(max_length=30, blank=False, null=False)  # Prénom
    # Email unique (utilisé comme identifiant)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False,
                            null=False)  # Numéro de téléphone
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)  # Photo de profil facultative
    # Statut actif de l'utilisateur
    is_active = models.BooleanField(default=True)
    # Détermine si l'utilisateur est un membre du staff
    is_staff = models.BooleanField(default=False)
    # Détermine si l'utilisateur est un administrateur
    is_admin = models.BooleanField(default=False)

    objects = UserManager()  # Utilisation du gestionnaire personnalisé

    USERNAME_FIELD = 'email'  # Champ utilisé comme identifiant pour l'authentification
    # Champs requis lors de la création d'un superutilisateur
    REQUIRED_FIELDS = ['pseudo', 'nom', 'prenom', 'phone']

    def __str__(self):
        """
        Retourne une représentation lisible de l'utilisateur.
        """
        return f"{self.nom} {self.prenom}"

    def has_perm(self, perm, obj=None):
        """
        Vérifie si l'utilisateur a une permission spécifique.
        Par défaut, retourne True.
        """
        return True

    def has_module_perms(self, app_label):
        """
        Vérifie si l'utilisateur a accès à un module spécifique.
        Par défaut, retourne True.
        """
        return True
