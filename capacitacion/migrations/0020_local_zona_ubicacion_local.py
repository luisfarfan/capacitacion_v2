# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-01 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0019_auto_20161130_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='zona_ubicacion_local',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]