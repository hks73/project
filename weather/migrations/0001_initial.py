# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='weatherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('temp', models.TextField()),
                ('humid', models.TextField()),
            ],
        ),
    ]
