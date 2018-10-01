from django import forms
from orders.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review     