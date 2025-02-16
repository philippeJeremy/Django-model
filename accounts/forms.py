from django import forms
from .models import User

# Formulaire de base pour la gestion des utilisateurs


class UserForm(forms.ModelForm):
    """
    Formulaire général pour l'utilisateur (utilisable par l'admin ou autre vue spécifique).
    """
    class Meta:
        model = User  # Utilisation du modèle User
        fields = ['pseudo', 'profile_picture', 'nom', 'prenom', 'email', 'phone',
                'profile_picture', 'is_active', 'is_staff', 'is_admin'] # Champs affichés dans le formulaire


# Formulaire d'inscription des utilisateurs
class RegistrationForm(forms.ModelForm):
    """
    Formulaire d'inscription pour les nouveaux utilisateurs.
    """
    password = forms.CharField(
        widget=forms.PasswordInput)  # Champ pour le mot de passe
    # Confirmation du mot de passe
    password_2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['pseudo', 'profile_picture', 'nom', 'prenom',
                'email', 'phone', 'password']  # Champs du formulaire

    def clean_email(self):
        """
        Vérifie si l'email est déjà utilisé dans la base de données.
        """
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            # Erreur si l'email est déjà utilisé
            raise forms.ValidationError("Cet e-mail est déjà pris.")
        return email

    def clean(self):
        """
        Vérifie si les mots de passe correspondent.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            # Ajoute une erreur si les mots de passe ne sont pas identiques
            self.add_error(
                "password_2", "Les mots de passe doivent correspondre.")
        return cleaned_data

    def save(self, commit=True):
        """
        Enregistre un nouvel utilisateur avec un mot de passe haché.
        """
        user = super().save(commit=False)
        # Hachage du mot de passe
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# Formulaire de création d'un utilisateur par un administrateur
class UserAdminCreationForm(forms.ModelForm):
    """
    Formulaire permettant à un administrateur de créer un nouvel utilisateur.
    """
    password = forms.CharField(
        widget=forms.PasswordInput)  # Champ pour le mot de passe
    # Confirmation du mot de passe
    password_2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['pseudo', 'profile_picture', 'nom', 'prenom', 'email',
                'phone', 'password']  # Champs inclus dans le formulaire

    def clean(self):
        """
        Vérifie si les mots de passe correspondent.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            # Ajoute une erreur si les mots de passe ne correspondent pas
            self.add_error(
                "password_2", "Les mots de passe doivent correspondre.")
        return cleaned_data

    def save(self, commit=True):
        """
        Enregistre un utilisateur avec un mot de passe haché.
        """
        user = super().save(commit=False)
        # Hachage du mot de passe
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# Formulaire de mise à jour des informations de l'utilisateur
class UserUpdateForm(forms.ModelForm):
    """
    Formulaire permettant à un utilisateur de mettre à jour ses informations personnelles.
    """
    class Meta:
        model = User
        fields = ['pseudo', 'nom', 'prenom', 'email', 'phone',
                'profile_picture']  # Champs modifiables par l'utilisateur
