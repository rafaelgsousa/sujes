from rest_framework import serializers

from ..models import *


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'address']


class SchoolSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSerie
        fields = ['serie']


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['name', 'year', 'school_serie']


class SchoolroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schoolroom
        fields = ['name', 'school', 'school_class']


class SchoolSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSubjects
        fields = ['name', 'employee', 'school_class']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields= ['start_class', 'end_class', 'school_subject']


class PresenceInClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresenceInClass
        fields = ['present', 'student', 'class_room']

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = ['grade', 'month', 'year', 'type', 'student', 'school_subject']