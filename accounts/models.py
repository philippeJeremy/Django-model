from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstracBaseUser, PermissionMixin

class UserManager(BaseUserManager):

		def create_user(self, email, nom, prenom, telephone, password=None):
				if not email:
						raise ValueError("les utilisateurs doivent avoir un email")
		
		user = self.model(
				email=self.normalize_email(email),
				nom=nom,
				prenom=prenom,
				telephone=telephone)
		user.set_password(password)
		user.save(using=self._db)
		
		return user
		
		def create_staffuser(self, email, nom, prenom, telephone, password=None):
				if not email:
						raise ValueError("les utilisateurs doivent avoir un email")
		
		user = self.create_user(
				email=self.normalize_email(email),
				nom=nom,
				prenom=prenom,
				telephone=telephone
				password=passord)
		user.is_staff = True
		user.save(using=self._db)
		
		return user
		
		def create_superuser(self, email, nom, prenom, telephone, password=None):
				if not email:
						raise ValueError("les utilisateurs doivent avoir un email")
		
		user = self.create_user(
				email=self.normalize_email(email),
				nom=nom,
				prenom=prenom,
				telephone=telephone
				password=passord)
		user.is_staff = True
		user.is_admin = True
		user.save(using=self._db)
		
		return user
		
class User(AbstracBaseUser, PermissionMixin):
		nom = models.CharField(max_length=30, blank=False, null=False)
		prenom = models.CharField(max_length=30, blank=False, null=False)
		email = models.EmailField(unique=True, blank=False, null=False)
		nom = models.CharField(max_length=30, blank=False, null=False)
		phone = models.CharField(max_length=15, blank=False, null=False)
		is_active = models.BooleanField(default=True)
		is_staff = models.BooleanField(default=False)
		is_admin = models.BooleanField(default=False)
		
		objects = UserManager()
		
		USERNAME_FIELD = 'email'
		REQUIRED_FIELDS = ['nom', 'prenom', 'telephone']
		
		def __str__(self):
				return f"{self.nom} {self.prenom}"
		
		def has_perm(self, perm, obj=None):
				return True
				
		def has_module_perms(self, app_label):
				return True