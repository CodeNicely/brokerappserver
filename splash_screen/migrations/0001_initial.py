# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='version_data',
            fields=[
                ('version_id', models.AutoField(primary_key=True, serialize=False)),
                ('version_no', models.SmallIntegerField(default=0)),
                ('compulsory_update', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
