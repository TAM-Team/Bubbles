import datetime

from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.forms import ModelForm
from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

HELP_STATUS_CHOICES = [
    ('Needed', 'Needs Help'),
    ('Not_Needed', 'Has been helped'),
    ('Being', 'Being helped'),
]


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    profile_picture = models.ImageField(blank=True, null=True, upload_to="i/")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=2225, default="Mount Albert, Auckland, New Zealand")
    # user_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

    def get_name(self):
        return "" + self.first_name + " " + self.last_name
    # def get_image(self):
    #     if (self.profile_picture != null):
    #         return self.profile_picture
    #     else:
    #         return "Error"


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    def get_absolute_url(self):
        return '/%s/' % self.name


class Post(models.Model):
    post_title = models.CharField("Post Title", max_length=255)
    description = models.TextField("Description")
    help_status = models.TextField(choices=HELP_STATUS_CHOICES)
    poster = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_date = models.DateTimeField("Created Date", default=datetime.datetime.now, blank=True)
    def __str__(self):
        return self.post_title

    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=7)

    def get_absolute_url(self):
        return '/%s/' % self.name

    class Meta:
        ordering = ['created_date']


class Helper(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=True)
    helper = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class Event(models.Model):
    event_title = models.CharField("Event Title", max_length=255)
    location = models.CharField("Location", max_length=2225, default="Unitec Institute of Technology, Mt Albert Campus Map Carrington Road, Mount Albert, Auckland, New Zealand")

    description = models.TextField("Description")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    start_time = models.TimeField("Start Time")
    end_time = models.TimeField("End Time")
    attachment = models.FileField("Attach File", null=True,blank=True)
    organiser = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.event_title

    def get_absolute_url(self):
        return '/%s/' % self.name


class Assisstant(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    helper = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post
