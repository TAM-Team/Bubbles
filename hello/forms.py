import posixpath

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput
from django.forms import ModelForm, models, DateTimeInput
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from hello.models import User, Post, Event
from datetimepicker.widgets import DateTimePicker


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


# Custom image Widget
def thumbnail(image_path, width, height):
    absolute_url = posixpath.join(settings.MEDIA_URL, image_path)
    return '<img src="%s" alt="%s" class="widget-img" />' % (absolute_url, image_path)


class ImageWidget(forms.ClearableFileInput):
    template = '<div>%(image)s</div>' \
               '<div>%(clear_template)s</div>' \
               '<div>%(input)s</div>'

    def __init__(self, attrs=None, template=None, width=200, height=200):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        if not self.is_required:
            checkbox_name = self.clear_checkbox_name(name)
            checkbox_id = self.clear_checkbox_id(checkbox_name)
            substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
            substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
            substitutions['clear'] = forms.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})

        input_html = super(forms.ClearableFileInput, self).render(name, value, attrs, renderer=None)
        if value and hasattr(value, 'width') and hasattr(value, 'height'):
            image_html = thumbnail(value.name, self.width, self.height)
            output = self.template % {'input': input_html,
                                      'image': image_html,
                                      'clear_template': self.template_with_clear % substitutions}
        else:
            output = input_html
        return mark_safe(output)


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ['address']
#     def __init__(self, *args, **kwargs):
#         super(AddressForm, self).__init__(*args, **kwargs)
#         self.fields['address'].widget = TextInput(attrs={
#             'id': 'address-field-id',
#             'class': 'myCustomClass',
#             'name': 'address-field'})

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["profile_picture", "email", "first_name", "last_name", "address", "password1", "password2"]
        # widgets = {'profile_picture': ImageWidget}


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("profile_picture", "email", "first_name", "last_name", "address")
        # widgets = {'profile_picture': ImageWidget}


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'description', 'help_status', 'created_date')

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(CreatePostForm, self).save(commit=False)
        inst.poster = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_title', 'description', 'location', 'start_date_time', 'end_date_time', 'attachment')
        #widgets = {'start_date_time': super.start_time}

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(CreateEventForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(CreateEventForm, self).save(commit=False)
        inst.organiser = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst
