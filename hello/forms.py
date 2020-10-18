from django import forms
from django.contrib.auth.forms import UserCreationForm

from hello.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["profile_picture", "email", "first_name", "last_name", "password1", "password2"]




# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('profile_picture',)

