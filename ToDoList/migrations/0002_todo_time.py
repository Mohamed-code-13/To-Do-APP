# Generated by Django 2.2.5 on 2019-12-18 23:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 23, 3, 0, 215192, tzinfo=utc)),
        ),
    ]