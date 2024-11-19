from django import forms
from djanbgo.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserForm(forms.ModelForm):
		class Meta:
				model = User
				field = ['nom', 'prenom', 'email', 'telephone', 'is_active', 'is_staff', 'is_admin']
				
class RegistrationForm(forms.modelForm):
		"""
		Formulaire d'inscription pour les utilisateurs.
		"""
		password = forms.Charfield(widget=forms.PasswordInput)
		password_2 = forms.Charfield(label='Confirm Password', widget=forms.PasswordInput)
		
		class Meta:
				model = User
				field = ['nom', 'prenom', 'email', 'telephone', 'password']
				
		def clean_email(self):
				email = self.cleaned_data.get("email")
				qs = User.objects.filter(email=email)
				if qs.exists():
						raise forms.ValidationError("Cet email est déjà pris")
				return email
				
		def clean(self):
				cleaned_data = super().clean()
				password = cleaned_data.get(password")
				password_2 = cleaned_data.get(password_2")
				if password in not None and password != password_2:
						self.add_error("password_2", "Les mots de passe doivent correspondre.")
				return cleaned_data
				
		def save(self, commit=True):
				user = super().save(commit=False)
				user.set_password(self.cleaned_data["password"])
				if commit:
					user.save()
				return user
				
class UserAdminCreationForm(forms.ModelForm):
		"""
		Formulaire de création d'un nouvel utilisateur par l'administreateur.
		"""
		password = forms.Charfield(widget=forms.PasswordInput)
		password_2 = forms.Charfield(label='Confirm Password', widget=forms.PasswordInput)
		
		class Meta:
				model = User
				field = ['nom', 'prenom', 'email', 'telephone', 'password']
				
		def clean_email(self):
				email = self.cleaned_data.get("email")
				qs = User.objects.filter(email=email)
				if qs.exists():
						raise forms.ValidationError("Cet email est déjà pris")
				return email
				
		def clean(self):
				cleaned_data = super().clean()
				password = cleaned_data.get(password")
				password_2 = cleaned_data.get(password_2")
				if password in not None and password != password_2:
						self.add_error("password_2", "Les mots de passe doivent correspondre.")
				return cleaned_data
				
		def save(self, commit=True):
				user = super().save(commit=False)
				user.set_password(self.cleaned_data["password"])
				if commit:
					user.save()
				return user
		
class UserAdminChangeForm(forms.ModelForm):
		"""
		Formulaire pour mettre à jour les informations des utilisateurs dans l'administration.
		"""
		password = ReadOnlyPasswordHashField()
		
		class Meta:
				model = User
				field = ['nom', 'prenom', 'email', 'telephone', 'password', 'is_staff', 'is_admin']
		
		def clean_password(self):
				return self.initial["password"]
		