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
    fname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    lname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    phone_number = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    pincode = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    add1 = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    add2 = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    city = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    state= forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}),
    )
    class Meta:
        model = Address
        fields = ["fname","lname","email","phone_number","pincode","add1","add2","city","state"]

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
