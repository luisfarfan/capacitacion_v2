# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0006_local_cantidad_usar_aulas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localambiente',
            name='cantidad_disponible',
        ),
        migrations.RemoveField(
            model_name='localambiente',
            name='cantidad_utilizar',
        ),
    ]