# Generated by Django 5.0.1 on 2024-02-08 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='presence_in_class',
            new_name='PresenceInClass',
        ),
        migrations.RenameModel(
            old_name='School_class',
            new_name='SchoolClass',
        ),
        migrations.RenameModel(
            old_name='School_serie',
            new_name='SchoolSerie',
        ),
        migrations.RenameModel(
            old_name='School_supplies',
            new_name='SchoolSubjects',
        ),
        migrations.RenameModel(
            old_name='test_score',
            new_name='TestScore',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='school_class_id',
            new_name='school_class',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='user_id',
            new_name='user',
        ),
    ]
