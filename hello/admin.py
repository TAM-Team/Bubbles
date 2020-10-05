from django.contrib import admin

# Register your models here.

from .models import Post, Event

admin.site.register(Post)
admin.site.register(Event)
