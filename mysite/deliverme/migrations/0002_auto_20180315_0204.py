# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.AddField(
            model_name='post',
            name='destLat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='destLon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='locLat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='locLon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]