# Generated by Django 3.2.6 on 2021-10-14 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0002_registration_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='dob',
        ),
    ]
