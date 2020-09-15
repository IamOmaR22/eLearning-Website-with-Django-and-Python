from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    pass
