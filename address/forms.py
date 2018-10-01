from django import forms
from .models import Addrss
 
 
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['fullname', 'mobile', 'pincode', 'town', 'state', 'house','area','landmark',]