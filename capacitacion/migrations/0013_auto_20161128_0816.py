# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0012_auto_20161128_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='local',
            old_name='capacidad_local',
            new_name='capacidad_local_disponible',
        ),
        migrations.AddField(
            model_name='local',
            name='capacidad_local_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='capacidad_local_usar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
