from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('password_reset/', views.PasswordResetViewCustom.as_view(), name='password_reset'),
]