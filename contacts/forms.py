from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message', 'checkin', 'checkout']
        widgets = {
            'message' : forms.Textarea(attrs={
            'class' : 'form-control',
            'row' : 5,
            'placeholder' : 'Enter your message here...'
            }),
        }