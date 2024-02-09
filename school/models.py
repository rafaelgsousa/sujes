from datetime import datetime
from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from persons.models import CustomUser, Role


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SchoolSerie(models.Model):
    serie = models.CharField(max_length=10)

    def __str__(self):
        return self.serie

class SchoolClass(models.Model):
    name = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    school_serie = models.ForeignKey(SchoolSerie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school_serie.serie} - {self.name}'

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    cpf = models.CharField(max_length=12)
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=255)
    role = models.ManyToManyField(Role)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} - {self.role.all()[0]}'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    rented = models.IntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} - matriculado no(a) {self.school_class.name}'

class Schoolroom(models.Model):
    name = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school.name} sala - {self.name}'

class SchoolSubjects(models.Model):
    name = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} sala - {self.school_class.name}'


class Classroom(models.Model):
    start_class = models.DateTimeField()
    end_class = models.DateTimeField()
    school_subject = models.ForeignKey(SchoolSubjects, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school_subject.name} de {self.start_class} à {self.end_class}'

class PresenceInClass(models.Model):
    present = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.fullname} - aula de {self.classroom.start_class} a {self.classroom.end_class}'

class TestScore(models.Model):
    class TypeTestScore(models.IntegerChoices):
        MONTHLY = 0, 'Monthly'
        BIMONTHLY = 1, 'bimonthly'
        BIMMONTHLY_RECOVERY = 2, 'bimonthly recovery'
        SEMI_ANNUAL_RECOVERY = 3, 'semi-annual recovery'
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=5)
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], default=datetime.now().month)
    year = models.IntegerField(default=datetime.now().year)
    type = models.CharField(choices=TypeTestScore.choices, default=TypeTestScore.MONTHLY)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_subject = models.ForeignKey(SchoolSubjects, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.user.first_name} - {self.school_subject.name}'