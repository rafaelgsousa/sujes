# Generated by Django 5.0.1 on 2024-02-12 14:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_testscore_grade_testscore_month_testscore_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('entre_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='rented',
        ),
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renta_date', models.DateTimeField(auto_now_add=True)),
                ('expected_return', models.DateTimeField(default=datetime.datetime(2024, 2, 19, 14, 17, 11, 85595, tzinfo=datetime.timezone.utc))),
                ('return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.book')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.employee')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
    ]
