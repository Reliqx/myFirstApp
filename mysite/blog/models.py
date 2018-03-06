from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
