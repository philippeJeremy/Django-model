from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, PasswordResetView

from .forms import RegistrationForm, UserUpdateForm

class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')  # Remplacez par votre URL de redirection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'signup'
        context['lien'] = 'lien_signup'
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['page'] = 'profile'
        context['lien'] = 'lien_profile'
        return context 

class ModifierProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Si vous utilisez un modèle utilisateur personnalisé
    form_class = UserUpdateForm
    template_name = 'accounts/modifier_profile.html'
    success_url = reverse_lazy('accounts:profile')  # Redirige vers la page de profil

    def get_object(self):
        return self.request.user  # Charge l'utilisateur connecté


class LoginViewCustom(LoginView):
    template_name = 'registration/login.html'
    
    def get_context_data(self, **kwargs):
        extra_context = super().get_context_data(**kwargs)
        extra_context = {"page" : "login", "lien": "lien_login"}
        extra_context['form'] = self.get_form()
        return extra_context
    
class PasswordResetViewCustom(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    
    def get_context_data(self, **kwargs):
        extra_context = super().get_context_data(**kwargs)
        extra_context = {"page" : "password"}
        extra_context['form'] = self.get_form()
        return extra_context
    
    


