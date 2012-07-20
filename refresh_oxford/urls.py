from django.conf import settings
from django.conf.urls import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import SignUp


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^code-of-conduct/$', TemplateView.as_view(template_name='code-of-conduct.html'), name='code-of-conduct'),
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'static/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

