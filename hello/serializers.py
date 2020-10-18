from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from hello.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'profile_picture']

class CustomRegisterSerializer(RegisterSerializer):
    profile_picture = serializers.ImageField(
        required=False,
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['profile_picture'] = self.validated_data.get('profile_picture', '')
        return data_dict