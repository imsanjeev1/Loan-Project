# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-13 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('emailid', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'registered_users',
            },
        ),
        migrations.CreateModel(
            name='LoanEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('loan_amount', models.CharField(max_length=50)),
                ('earn_amount', models.IntegerField()),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'loan_table',
            },
        ),
    ]
