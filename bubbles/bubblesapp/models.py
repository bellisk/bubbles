from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

INTERVALS = (
    (1, "Every day"),
    (3, "Every three days"),
    (7, "Every week"),
    (14, "Every two weeks"),
    (30, "Every month"),
    (90, "Every three months"),
    (365, "Every year")
)

THRESHOLDS = (
    (2, "twice"),
    (5, "five times"),
    (10, "ten times")
)

class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profiles")
    reminder_interval = models.IntegerField(choices=INTERVALS)
    reminder_threshold = models.IntegerField(choices=THRESHOLDS)
    def __unicode__(self):
        return self.user.username

class Contact(models.Model):
    profile = models.ForeignKey(Profile, related_name="contacts")
    name = models.CharField(max_length=200)
    last_contact = models.DateField()
    frequency = models.IntegerField(choices=INTERVALS)
    def __unicode__(self):
        return self.name


