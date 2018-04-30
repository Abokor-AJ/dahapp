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
                                widget=forms.TextInput(attrs={'placeholder': 'Cheque number'}))
    bank_name = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Bank Name'}))
    customer_name = forms.CharField(max_length=50,
                                    widget=forms.TextInput(attrs={'placeholder': 'Customer Name'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2,
                                widget=forms.TextInput(attrs={'placeholder': 'Amount'}))
    currency = forms.CharField(max_length=5,
                               widget=forms.TextInput(attrs={'placeholder': 'currency'}))

    class Meta:
        model = Cheque
        fields = ('cheque_no', 'bank_name', 'customer_name', 'amount', 'currency',)

    def clean(self):
        cd = super(ChequeForm, self).clean()
        cheque_no = cd.get('cheque_no')
        bank_name = cd.get('bank_name')
        customer_name = cd.get('customer_name')
        amount = cd.get('amount')
        currency = cd.get('currency')
        if not cheque_no and not bank_name:
            raise forms.ValidationError('Please enter the correct data.')
