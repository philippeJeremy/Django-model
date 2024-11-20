from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import RegistrationForm, UserUpdateForm

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "accounts/signup.html", 
                  context={"form": form, "page" : "signup"})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vos informations ont été mises à jour avec succès.')
            return redirect('profile')  # Redirection après la mise à jour
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})


class LoginViewCustom(LoginView):
    template_name = 'registration/login.html'
    
    def get_context_data(self, **kwargs):
        extra_context = super().get_context_data(**kwargs)
        extra_context = {"page" : "signup", "lien": "lien"}
        extra_context['form'] = self.get_form()
        return extra_context
    
class PasswordResetViewCustom(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    
    def get_context_data(self, **kwargs):
        extra_context = super().get_context_data(**kwargs)
        extra_context = {"page" : "password"}
        extra_context['form'] = self.get_form()
        return extra_context
    
    


