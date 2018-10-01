from django import forms
from .models import Order
from django.core.validators import RegexValidator
 
 
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        mobile = forms.CharField(validators=[phone_regex], max_length=17,) # validators should be a list
        fields = ['fullname', 'mobile', 'pincode', 'town', 'state', 'house','area','landmark',]