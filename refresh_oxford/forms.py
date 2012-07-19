from django import forms

from .models import Attendee


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Attendee

