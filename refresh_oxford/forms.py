from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Attendee


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Attendee

    helper = FormHelper()
    helper.form_method = 'post'
    helper.layout = Layout(
        Fieldset('',
            'name',
            'email',
            'github_username',
            'extra',
            Submit('submit', _('Sign Up'), css_class='submit'),
        )
    )
