from django.db import models
from django.utils.translation import ugettext_lazy as _
from feincms.content.richtext.models import RichTextContent
from feincms.module.page.models import Page


class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    github_username = models.CharField(max_length=255, null=True, blank=True)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('pk',)

    def __unicode__(self):
        return self.name


class MailingListPerson(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


Page.register_templates(
    {
        'key': '1col',
        'title': _('One column'),
        'path': 'base.html',
        'regions': (
            ('main', _('Main content')),
        ),
    },
)
Page.create_content_type(RichTextContent)

