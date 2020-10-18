from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import Post, Event


UserAdmin.ordering = ('email',)
#Define an inline admin descriptor for User_Profile model
#which acts a bit like a singleton
# class UserInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
# #Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (UserInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Event)