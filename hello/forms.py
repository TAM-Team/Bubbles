from django import forms
from django.contrib.auth.forms import UserCreationForm

from hello.models import User, Post


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["profile_picture", "email", "first_name", "last_name", "password1", "password2"]


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('profile_picture', "email", "first_name", "last_name")


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_title', 'description', 'help_status', 'poster', 'created_date')