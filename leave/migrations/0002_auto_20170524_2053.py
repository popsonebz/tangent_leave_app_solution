# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='start_date',
            field=models.DateField(),
        ),
    ]
