from django.conf import settings
from django.conf.urls import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import Home, SignUp


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'static/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),

    url('', include('feincms.urls')),
)

urlpatterns += staticfiles_urlpatterns()

