# Generated by Django 2.2 on 2020-05-19 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20200519_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_datetime',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 248115)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 248131)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_datetime',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 248096)),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='end_datetime',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 248599)),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 248616)),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='start_datetime',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 248578)),
        ),
        migrations.AlterField(
            model_name='room',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 55, 16, 247740)),
        ),
    ]
