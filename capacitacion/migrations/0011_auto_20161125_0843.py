# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0010_auto_20161124_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursocriterio',
            old_name='peso',
            new_name='ponderacion',
        ),
        migrations.RemoveField(
            model_name='cursocriterio',
            name='descripcion_criterio',
        ),
    ]