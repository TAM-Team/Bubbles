import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class User(models.Model):
    username = models.TextField("Username")
    first_name = models.TextField("FirstName")
    last_name = models.TextField("LastName")
    email = models.TextField("Email")
    password = models.TextField("Password")
    def __str__(self):
        return self.username


class Post(models.Model):
    post_title = models.TextField("Post Title")
    location = models.TextField("Location")
    description = models.TextField("Description")
    help_status = models.TextField("Help status")

    def __str__(self):
        return self.post_title

class Event(models.Model):
    event_title = models.TextField("Event Title")
    location = models.TextField("Location")
    description = models.TextField("Description")
    start_date = models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("End Time")
    attachment = models.TextField("Attach File")
    def __str__(self):
        return self.event_title