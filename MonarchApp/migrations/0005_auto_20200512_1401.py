# Generated by Django 3.0.6 on 2020-05-12 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MonarchApp', '0004_auto_20200511_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_employee_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_phone_number',
        ),
    ]
