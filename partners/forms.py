from django import forms
from .models import *

class PartnersForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'