# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object2book', '0007_auto_20170708_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default=0, max_length=255),
        ),
    ]