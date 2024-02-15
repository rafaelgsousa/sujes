# Generated by Django 5.0.1 on 2024-02-13 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_rented_expected_return'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolserie',
            old_name='serie',
            new_name='ano',
        ),
        migrations.AddField(
            model_name='schoolserie',
            name='grau',
            field=models.CharField(default=None, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rented',
            name='expected_return',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 20, 18, 27, 4, 702266, tzinfo=datetime.timezone.utc)),
        ),
    ]