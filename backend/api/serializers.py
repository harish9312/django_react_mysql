#To convert the data into JSON

from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'userName', 'password', 'email', 'phoneNo')
        model = models.User