# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0002_auto_20160813_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanentries',
            name='loan_limit',
            field=models.IntegerField(default=10000),
        ),
    ]
