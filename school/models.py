from uuid import uuid4

from django.db import models

from persons.models import CustomUser, Role


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class School_serie(models.Model):
    serie = models.CharField(max_length=10)

class School_class(models.Model):
    name = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    school_serie = models.ForeignKey(School_serie, on_delete=models.CASCADE)

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    cpf = models.CharField(max_length=12)
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=255)
    role = models.ManyToManyField(Role)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    rented = models.IntegerField()
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_class_id = models.ForeignKey(School_class, on_delete=models.CASCADE)

class Schoolroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_class = models.ForeignKey(School_class, on_delete=models.CASCADE)

class School_supplies(models.Model):
    name = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    school_class = models.ForeignKey(School_class, on_delete=models.CASCADE)

class Classroom(models.Model):
    start_class = models.DateTimeField()
    end_class = models.DateTimeField()
    school_supplie = models.ForeignKey(School_supplies, on_delete=models.CASCADE)

class presence_in_class(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class test_score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_supplies = models.ForeignKey(School_supplies, on_delete=models.CASCADE)