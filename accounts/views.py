# accounts/views.py

from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileImageForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = ProfileImageForm  # Só a foto de perfil
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Sempre retorna o usuário logado para editar
        return self.request.user

    def test_func(self):
        # Só permite editar o próprio perfil
        return self.get_object() == self.request.user


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('profile')
