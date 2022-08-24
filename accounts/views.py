from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm


class SingUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')


class UserPanelView(generic.ListView):
    model = CustomUser
    template_name = 'registration/user_panel.html'
