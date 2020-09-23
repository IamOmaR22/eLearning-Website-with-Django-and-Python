from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

from django.contrib import messages



from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')   # After Creating Login Form Then Put 'login' Here.
    template_name = 'users/register.html'


@login_required
def profile(request):
    if request.method == 'POST':   # This Will Be Run When I Submit My Form. And Possibly Pass New Data.
        u_form = UserUpdateForm(request.POST, instance=request.user)  # request.POST To Pass The POST Data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # File Data (images) Users Try To Upload.

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {   # To Pass This Into Template We Used context.
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
