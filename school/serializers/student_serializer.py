from rest_framework import serializers

from ..models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'date_of_birth','age', 'address', 'rented', 'user', 'school_class']
