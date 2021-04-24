from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import AddressForm
from .models import Address

from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit  import CreateView

# Create your views here.
class Home(TemplateView):
    template_name='main/index.html'

class UserLogin(LoginView):
    template_name='main/login.html'
    redirect_authenticated_user =True
    
    def get_success_url(self):
        return reverse_lazy('home')

class UserSignUp(UserPassesTestMixin,CreateView):
    template_name='main/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    
    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        return reverse_lazy('signup')

class UserLogout(LogoutView):
    next_page='home'

class AddAddress(CreateView):
    template_name='main/add_address.html'
    form_class = AddressForm
    success_url = reverse_lazy('view_address')

class ViewAddress(ListView):
    template_name='main/view_address.html'
    context_object_name='address'
    model=Address

    
    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)
        return queryset



