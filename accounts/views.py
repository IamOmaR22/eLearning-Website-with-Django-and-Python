from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')   # After Creating Login Form Then Put 'login' Here.
    template_name = 'users/register.html'

@login_required
def profile(request):

    return render(request, 'users/profile.html')

