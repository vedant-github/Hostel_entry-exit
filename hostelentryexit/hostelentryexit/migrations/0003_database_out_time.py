# Generated by Django 4.1.7 on 2023-03-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0002_remove_database_out_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='out_time',
            field=models.BooleanField(default=False),
        ),
    ]
