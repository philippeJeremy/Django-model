from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User 
from .forms import UserForm, RegistrationForm


class LginViewCustom(LoginView):
		template_name = 'registration/login.html'
		
		def get_context_data(self, **kwargs):
				extra_context = super().get_context_data(**kwargs)
				extra_context = {"page" : "login"}
				extra_context['form] = self.get_form()
				return extra_context

class PasswordResetViewCustom(PasswordResetView):
		template_name  = 'registration/password_reset_form.html'
		
		def get_context_data(self, **kwargs):
				extra_context = super().get_context_data(**kwargs)
				extra_context = {"page" : "reset_password"}
				extra_context['form] = self.get_form()
				return extra_context

def signup(request):
		if request.method == "POST":
				form = RegistrationForm(request.POST)
				if form.is_valid():
						form.save()
						return redirect("/")
		else:
				form = RegistrationForm()
		return render(request, "accounts/signup.html", context={"form": form})
		
@login_required
def profile(request):
		user = request.user
		return render(request, "accounts/profile.html", {'user': user})
		
@login_required
@user_passes_test(lambda u: u.is_staff)
def liste_users(request):
		users = User.objects.all()
		return render(request, "accounts/liste_users.html", {'users': users})

@login_required
@user_passes_test(lambda u: u.is_staff)
def supprimer_user(request, user_id):
		users = User.get_object_or_404(User, id=user_id)
		if request.method == 'POST':
				user.delete()
				return redirect("accounts/liste_users.html")
		return render(request, "accounts/confirmer_suppression.html", {'user': user})
		
@login_required
@user_passes_test(lambda u: u.is_staff)
def modifier_user(request, user_id):
		users = User.get_object_or_404(User, id=user_id)
		if request.method == 'POST':
				form = UserForm(request.POST, instance=user)
				if form.is_valid():
						form.save()
						return redirect("accounts/liste_users.html")
		else:
				form = UserForm(instance=user)
		return render(request, 'accounts/modifier_user.html', {'form': form, 'user': user})
		
