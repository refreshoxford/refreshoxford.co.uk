from django.contrib import messages
from django.views.generic import CreateView

from .forms import SignUpForm
from .models import Attendee


class Home(CreateView):
    form_class = None
    model = None
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['attendees'] = Attendee.objects.all()
        return context


class SignUp(CreateView):
    form_class = SignUpForm
    model = Attendee
    success_url = '/'
    template_name = 'signup.html'

    def form_valid(self, form):
        msg = "Thanks for signing up, we'll email you more details closer to the date."
        messages.info(self.request, msg)
        return super(SignUp, self).form_valid(form)

