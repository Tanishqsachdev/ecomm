from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.
class Home(TemplateView):
    template_name='main/index.html'

class UserLogin(LoginView):
    template_name='main/login.html'
    redirect_authenticated_user =True
    
    def get_success_url(self):
        return reverse_lazy('home')



