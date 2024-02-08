from uuid import uuid4

from django.contrib.auth.models import (AbstractUser, BaseUserManager, Group,
                                        Permission)
from django.db import models

from project import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field is mandatory')
        email = self.normalize_email(email)     
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomGroup(Group):
    user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='custom_groups')

class CustomPermission(Permission):
    user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='custom_permissions')
    

class CustomUser(AbstractUser):

    class LoginError(models.IntegerChoices):
        ZERO = 0, 'Zero'
        UM = 1, 'Um'
        DOIS = 2, 'Dois'
        TRES = 3, 'Tres'
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_logged = models.BooleanField(default=False)
    login_erro = models.IntegerField(choices=LoginError.choices, default=LoginError.ZERO)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email

class Phone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=10)
    number = models.CharField(max_length=20) # se é pai, mãe, tio, avó, atc ...
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    cpf = models.CharField(max_length=12)
    date_of_birth = models.DateTimeField()
    role = models.ManyToManyField(Role)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    rented = models.IntegerField()
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school_class_id = models.ForeignKey(School_class)

    

class Role(models.Model):
    name = models.CharField(max_length=50)

class VerificationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    code_verificated = models.BooleanField(default=False)


# class Device(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

# class Logger(models.Model):
#     endpoint = models.CharField(max_length=255)
#     user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
#     method = models.CharField(max_length=10)
#     body= models.CharField(max_length=255, null=True, blank=True)
#     view = models.CharField(max_length=255)
#     status = models.IntegerField()
#     invocation_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.endpoint} - {self.user} - {self.method} - {self.status}"
