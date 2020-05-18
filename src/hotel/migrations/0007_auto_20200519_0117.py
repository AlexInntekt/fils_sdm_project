# Generated by Django 2.2 on 2020-05-18 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20200518_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 1, 17, 2, 483884)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 1, 17, 2, 483863)),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='end_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 1, 17, 2, 484369)),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='start_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 1, 17, 2, 484345)),
        ),
        migrations.AlterField(
            model_name='room',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 1, 17, 2, 483483)),
        ),
    ]
