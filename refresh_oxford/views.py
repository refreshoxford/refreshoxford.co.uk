from django.views.generic import CreateView

from .forms import SignUpForm
from .models import Attendee


class SignUp(CreateView):
    form_class = SignUpForm
    model = Attendee
    success_url = '/'
    template_name = 'signup.html'

