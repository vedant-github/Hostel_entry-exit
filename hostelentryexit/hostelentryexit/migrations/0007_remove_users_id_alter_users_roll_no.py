# Generated by Django 4.1.7 on 2023-02-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelentryexit', '0006_alter_database_rollnum_1_alter_database_rollnum_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='roll_no',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]