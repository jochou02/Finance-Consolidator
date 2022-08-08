from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import *

class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'