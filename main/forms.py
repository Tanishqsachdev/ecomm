from django.forms import ModelForm
from .models import Address

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['building_number','street_name','locality','city','state','pincode']
