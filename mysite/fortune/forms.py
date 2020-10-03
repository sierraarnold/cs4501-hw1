from django import forms

class VerifyForm(forms.Form):
    verification_number = forms.CharField(label='Key:', max_length=50)
