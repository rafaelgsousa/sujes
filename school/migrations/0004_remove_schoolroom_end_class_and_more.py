# Generated by Django 5.0.1 on 2024-02-08 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_school_supplie_classroom_school_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolroom',
            name='end_class',
        ),
        migrations.RemoveField(
            model_name='schoolroom',
            name='start_class',
        ),
    ]