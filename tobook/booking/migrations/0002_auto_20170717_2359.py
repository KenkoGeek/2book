# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 23:59
from __future__ import unicode_literals

import booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pnr',
            field=models.CharField(default=booking.models.Booking.pnr, max_length=6, unique=True),
        ),
    ]
