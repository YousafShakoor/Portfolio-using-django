from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=['username','email','message']
