from django.forms import ModelForm
from .models import Address,Product

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['building_number','street_name','locality','city','state','pincode']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
