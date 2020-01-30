from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, FormView, CreateView

from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login_customer')
    template_name = 'registration/signup.html'

