from django.db import models


class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    github_username = models.CharField(max_length=255, null=True, blank=True)
    extra = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name
