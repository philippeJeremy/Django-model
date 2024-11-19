from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
			path('signup/', views.signup, name='signup'),
			path('liste_users/', views.liste_users, name='liste_users'),
			path('modifier_user/<int:user_id>/', views.modifier_user, name='modifier_user'),
			path('supprimer_user/<int:user_id>/', views.supprimer_user, name='sisupprimer_usernup'),
			path('profile/', views.profile, name='profile'),
			path('login/', views.LoginViewsCustom, name='login'),
			path('password_reset/', views.PasswordResetViewCustom, name='password_reset'),
			]
			