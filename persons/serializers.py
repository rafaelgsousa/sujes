from rest_framework import serializers

from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'picture','login_erro', 'is_active']

    password = serializers.CharField(write_only=True, required=True)
    id = serializers.UUIDField(read_only=True)