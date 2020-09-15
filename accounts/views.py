from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')   # After Creating Login Form Then Put 'login' Here.
    template_name = 'users/register.html'
