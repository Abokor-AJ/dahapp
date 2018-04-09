from django import forms
from .models import *
from django.contrib import messages
# from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RemitForm(forms.ModelForm):
    usd = forms.DecimalField(max_digits=10, decimal_places=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter USD Amount'})
                             )
    djf = forms.DecimalField(max_digits=12, decimal_places=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter DJF Amount'})
                             )

    class Meta:
        model = Remittance
        fields = ('usd', 'djf',)

    def clean(self):
        cd = super(RemitForm, self).clean()
        usd = cd.get('usd')
        djf = cd.get('djf')
        if not usd and not djf:
            raise forms.ValidationError('You have to enter the usd and djf amounts!')


class PayForm(forms.ModelForm):
    usd = forms.DecimalField(max_digits=10, decimal_places=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter USD Amount'}))
    djf = forms.DecimalField(max_digits=12, decimal_places=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter DJF Amount'}))

    class Meta:
        model = Payment
        fields = ('usd', 'djf',)

    def clean(self):
        cd = super(PayForm, self).clean()
        usd = cd.get('usd')
        djf = cd.get('djf')
        if not usd and not djf:
            raise forms.ValidationError('You have to enter the usd and djf amounts!')


class ChequeForm(forms.ModelForm):
    cheque_no = forms.CharField(max_length=15,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Cheque number'}))
    bank_name = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Bank Name'}))
    customer_name = forms.CharField(max_length=50,
                                    widget=forms.TextInput(attrs={'placeholder': 'Enter Customer Name'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Amount'}))
    currency = forms.CharField(max_length=5)

    class Meta:
        model = Cheque
        fields = ('cheque_no', 'bank_name', 'customer_name', 'amount', 'currency',)
