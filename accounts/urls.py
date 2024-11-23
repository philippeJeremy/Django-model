from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('modifier_profile/', views.ModifierProfileView.as_view(), name="modifier_profile"),
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('password_reset/', views.PasswordResetViewCustom.as_view(), name='password_reset'),
]