from django import forms
from django.contrib.auth.models import User
from authentication.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
        ]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "password": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "email": forms.EmailInput(attrs={'class': 'form-control ppap-form-field'}),
        }

class EmbracoUserForm(forms.ModelForm):
    class Meta:
        model = EmbracoProfile
        fields = [
            "department",
            "jobTitle",
            "phoneNumber",
            "is_administrator",
        ]
        widgets = {
            "department": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "jobTitle": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "phoneNumber": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "is_administrator": forms.CheckboxInput(attrs={'class': 'form-control ppap-form-field'}),
        }

class SupplierUserForm(forms.ModelForm):
    class Meta:
        model = SupplierProfile
        fields = [
            "supplierCode",
            "address",
            "country",
            "contactPerson",
            "phoneNumber",
        ]
        widgets = {
            "supplierCode": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "address": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "country": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "contactPerson": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "phoneNumber": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
        }
