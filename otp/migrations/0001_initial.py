# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='otp_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('otp', models.SmallIntegerField(default=0)),
                ('flag', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user_token_data',
            fields=[
                ('id', models.PositiveSmallIntegerField(default=0, primary_key=True, serialize=False)),
                ('access_token', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
