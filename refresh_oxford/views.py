from django.contrib import messages
from django.views.generic import CreateView

from .forms import SignUpForm
from .models import Attendee


class SignUp(CreateView):
    form_class = SignUpForm
    model = Attendee
    success_url = '/'
    template_name = 'signup.html'

    def form_valid(self, form):
        msg = "Thanks for signing up, we'll email you more details closer to the date."
        messages.info(self.request, msg)
        return super(SignUp, self).form_valid(form)

