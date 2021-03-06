# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0003_loanentries_loan_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('loan_amount', models.CharField(max_length=50)),
                ('earn_amount', models.IntegerField()),
                ('loan_limit', models.IntegerField()),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'loan_eligibility',
            },
        ),
    ]
