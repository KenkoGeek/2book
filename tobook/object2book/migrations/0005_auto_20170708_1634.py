# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object2book', '0004_auto_20170708_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object2book.Statuses'),
        ),
    ]
