# Generated by Django 5.0.1 on 2024-02-12 21:58

import datetime
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cpf', models.CharField(max_length=12)),
                ('date_of_birth', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('role', models.ManyToManyField(to='persons.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
        migrations.CreateModel(
            name='Schoolroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolclass')),
            ],
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='school_serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolserie'),
        ),
        migrations.CreateModel(
            name='SchoolSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.employee')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolclass')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_class', models.DateTimeField()),
                ('end_class', models.DateTimeField()),
                ('school_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolsubject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_of_birth', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolclass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renta_date', models.DateTimeField(auto_now_add=True)),
                ('expected_return', models.DateTimeField(default=datetime.datetime(2024, 2, 19, 21, 58, 10, 846412, tzinfo=datetime.timezone.utc))),
                ('return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.book')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.employee')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
        migrations.CreateModel(
            name='PresenceInClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.BooleanField(default=False)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
        migrations.CreateModel(
            name='TestScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('month', models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('year', models.IntegerField(default=2024)),
                ('type', models.CharField(choices=[(0, 'Monthly'), (1, 'bimonthly'), (2, 'bimonthly recovery'), (3, 'semi-annual recovery')], default=0)),
                ('school_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolsubject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
    ]
