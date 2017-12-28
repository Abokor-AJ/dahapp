from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RemitForm(forms.Form):
    usd = forms.DecimalField(max_digits=10, decimal_places=2)
    djf = forms.DecimalField(max_digits=12, decimal_places=2)