from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from .import forms

def home(request):
    return render(request, 'home.html')


def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']), # Subject
                form.cleaned_data['suggestion'],  # Body
                '{name} <{email}>'.format(**form.cleaned_data),   # From email
                ['omarfaruk2468@omar.com'],  # Sent To
            )
            messages.add_message(request, messages.SUCCESS, 'Thanks For Your Suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})