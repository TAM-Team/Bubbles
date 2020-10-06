import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

HELP_STATUS_CHOICES = [
    ('Needed', 'Needs Help'),
    ('Not_Needed', 'Has been helped'),
    ('Being', 'Being helped'),
]


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    def get_absolute_url(self):
        return '/%s/' % self.name


class Address(models.Model):
    address = models.TextField("Address")
    suburb = models.TextField("Suburb")
    city = models.TextField("City")
    state = models.TextField("State", null=True, blank=True)
    country = models.TextField("Country")
    postcode = models.TextField("Postcode")
    def __str__(self):
        return self.address + "\n" + self.suburb
    def get_absolute_url(self):
        return '/%s/' % self.name



class Post(models.Model):
    post_title = models.CharField("Post Title", max_length=255)
    description = models.TextField("Description")
    help_status = models.TextField(choices=HELP_STATUS_CHOICES)
    #poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField("Created Date", default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.post_title

    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=7)
    def get_absolute_url(self):
        return '/%s/' % self.name


class Event(models.Model):
    event_title = models.TextField("Event Title")
    location = models.TextField("Location")
    description = models.TextField("Description")
    start_date = models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("End Time")
    attachment = models.TextField("Attach File")
    #organiser = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.event_title
    def get_absolute_url(self):
        return '/%s/' % self.name


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']