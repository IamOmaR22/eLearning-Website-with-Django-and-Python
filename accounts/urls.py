from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
]