from rest_framework import serializers

from ..models import *


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSerie
        fields = '__all__'


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = '__all__'


class SchoolroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schoolroom
        fields = '__all__'


class SchoolSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSubject
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields= '__all__'


class PresenceInClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresenceInClass
        fields = '__all__'

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class RentedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rented
        fields = '__all__'