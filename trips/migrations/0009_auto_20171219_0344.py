# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_trip_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='cost',
        ),
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
