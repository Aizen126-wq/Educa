# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile_image')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile_image')

class ProfileImageForm(forms.ModelForm):
    """Para o usuário atualizar só a foto de perfil no site."""
    class Meta:
        model = User
        fields = ['profile_image']
