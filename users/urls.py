from django.urls import path
from .views import ShowProfilePageView, UserRegisterView, UserEditView, PasswordsChangeView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views