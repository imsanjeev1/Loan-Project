# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-13 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authusers',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
