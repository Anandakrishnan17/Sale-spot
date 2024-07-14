# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    # Customize fields or labels as needed
    # Example: add a Remember Me checkbox
    remember_me = forms.BooleanField(label='Remember Me', required=False)
