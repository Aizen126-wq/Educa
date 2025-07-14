# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ['username', 'email', 'is_superuser']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'profile_image',
                'groups',
                'user_permissions'
            ),
        }),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_image',)}),
    )

admin.site.register(CustomUserModel, CustomUserAdmin)
