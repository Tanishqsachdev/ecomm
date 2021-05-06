from django.forms import ModelForm
from .models import Address,Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['building_number','street_name','locality','city','state','pincode']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
