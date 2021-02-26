from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:

        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        labels = {'email':'Email'}


class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User

        fields = ['username','password']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Re-enter New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}))
