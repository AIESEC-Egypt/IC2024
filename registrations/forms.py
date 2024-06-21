from django import forms
from .models import *

class DelegateForm(forms.ModelForm):
    
    new_username = forms.CharField(
        label=("Username"),
        max_length=150,
        required=True,
    )
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput,
        strip=False,
        required=True,
    )
    
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
        required=True,
    )


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('new_password1')
        confirm_password = cleaned_data.get('new_password2')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
    class Meta:
        model = Delegate
        exclude = ['name_as_per_passport', 'current_living_country_territory', 'passport_scanned_photo', 'passport_issue_date', 'passport_expiry_date', 'room_preference', 'food', 'allergies', 'pre_and_post_trips', 'merchandise', 'egyptian_nights_expectations', 'cc_team_expecations', 'logistical_expectations', 'agenda_expectations', 'visa_support', 'user']
        widgets = {
            'aiesec_email': forms.TextInput(attrs={'placeholder': 'ex: omar@aiesec.net'}),
            'personal_email': forms.TextInput(attrs={'placeholder': 'ex: omar@gmail.com'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'ex: +2010********'}),
            'telegram_username': forms.TextInput(attrs={'placeholder': 'ex: @omar'}),
            'age': forms.TextInput(attrs={'placeholder': 'ex: 24'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CheckInForm(forms.ModelForm):
    class Meta:
        model = Delegate
        fields = ['name_as_per_passport', 'natonality', 'current_living_country_territory', 'passport_scanned_photo', 'passport_issue_date', 'passport_expiry_date', 'room_preference', 'food', 'allergies', 'pre_and_post_trips', 'merchandise', 'egyptian_nights_expectations', 'cc_team_expecations', 'logistical_expectations', 'agenda_expectations', 'visa_support']
        widgets = {
            'passport_issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'passport_expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'allergies': forms.TextInput(attrs={'placeholder': "if you don't have please write 'none'"}),
            'expectation_from_cc_team': forms.TextInput(attrs={'placeholder': "if you don't have please write 'none'"}),
            'expectation_from_egyptian_nights': forms.TextInput(attrs={'placeholder': "if you don't have please write 'none'"}),
            'food': forms.CheckboxSelectMultiple(),
        }

class CustomPasswordChangeForm(forms.Form):
    username = forms.CharField(
        label=("Username"),
        max_length=150,
        required=True,
    )
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput,
        strip=False,
        required=True,
    )
    
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
        required=True,
    )


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('new_password1')
        confirm_password = cleaned_data.get('new_password2')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        

class DelegateUserForm(forms.Form):
    delegate_form = DelegateForm(prefix='delegate')
    user_form = CustomPasswordChangeForm(prefix='user')