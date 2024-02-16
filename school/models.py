from datetime import datetime, timedelta
from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from persons.models import CustomUser


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SchoolSerie(models.Model):
    ano = models.CharField(max_length=10)
    grau = models.CharField(max_length=25)

    def __str__(self):
        return self.serie

class SchoolClass(models.Model):
    name = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    school_serie = models.ForeignKey(SchoolSerie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school_serie.ano} - {self.name}'

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    cpf = models.CharField(max_length=12)
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} - {self.role.all()[0]}'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} - matriculado no(a) {self.school_class.school_serie.ano} - {self.school_class.name}'

class Schoolroom(models.Model):
    name = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school.name} sala - {self.name}'

class SchoolSubject(models.Model):
    name = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} sala - {self.school_class.name}'


class Classroom(models.Model):
    start_class = models.DateTimeField()
    end_class = models.DateTimeField()
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE)

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
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.user.first_name} - {self.school_subject.name}'

class Book(models.Model):
    name = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book} - {self.codigo}'
    
class Rented(models.Model):
    renta_date = models.DateTimeField(auto_now_add=True)
    expected_return = models.DateTimeField(default=timezone.now() + timedelta(days=7))
    return_date = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book} - {self.student} - renta_date = {self.renta_date} expexted_return = {self.expected_return}'