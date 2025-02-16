from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, PasswordResetView

from .forms import RegistrationForm, UserUpdateForm


class SignupView(CreateView):
    """
    View for user registration (sign up).
    """
    form_class = RegistrationForm  # Form used for registration
    # Template for rendering the sign-up page
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')  # Redirect URL after successful sign-up

    def get_context_data(self, **kwargs):
        """
        Add additional context data for rendering the sign-up page.
        """
        context = super().get_context_data(**kwargs)
        # Additional context for page identification
        context['page'] = 'signup'
        # Additional context for link identification
        context['lien'] = 'lien_signup'
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    """
    View for user profile page.
    Requires login.
    """
    template_name = 'accounts/profile.html'  # Template for rendering the profile page

    def get_context_data(self, **kwargs):
        """
        Add additional context data for rendering the profile page.
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Current logged-in user
        # Additional context for page identification
        context['page'] = 'profile'
        # Additional context for link identification
        context['lien'] = 'lien_profile'
        return context


class ModifierProfileView(LoginRequiredMixin, UpdateView):
    """
    View for updating user profile information.
    Requires login and updates the current user's information.
    """
    model = get_user_model()  # User model for updating user information
    form_class = UserUpdateForm  # Form used for updating user profile
    # Template for rendering the profile update page
    template_name = 'accounts/modifier_profile.html'
    # Redirect URL after successful profile update
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        """
        Get the current user object for updating.
        """
        return self.request.user  # Return the current logged-in user object


class LoginViewCustom(LoginView):
    """
    Custom login view.
    """
    template_name = 'registration/login.html'  # Template for rendering the custom login page

    def get_context_data(self, **kwargs):
        """
        Add additional context data for rendering the custom login page.
        """
        extra_context = super().get_context_data(**kwargs)
        # Additional context for page and link identification
        extra_context = {"page": "login", "lien": "lien_login"}
        extra_context['form'] = self.get_form()  # Form instance for login
        return extra_context


class PasswordResetViewCustom(PasswordResetView):
    """
    Custom password reset view.
    """
    template_name = 'registration/password_reset_form.html'  # Template for rendering the custom password reset page

    def get_context_data(self, **kwargs):
        """
        Add additional context data for rendering the custom password reset page.
        """
        extra_context = super().get_context_data(**kwargs)
        # Additional context for page identification
        extra_context = {"page": "password"}
        # Form instance for password reset
        extra_context['form'] = self.get_form()
        return extra_context
