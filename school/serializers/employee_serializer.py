from rest_framework import serializers

from ..models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'cpf', 'date_of_birth', 'address', 'role', 'user']