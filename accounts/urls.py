# accounts/urls.py

from django.urls import path
from .views import SignupView, ProfileView, CustomPasswordChangeView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
