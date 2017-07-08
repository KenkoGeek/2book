# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object2book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='remaining',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='object2book.Statuses'),
        ),
    ]