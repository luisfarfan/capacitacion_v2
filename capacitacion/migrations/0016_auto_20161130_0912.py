# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0015_auto_20161128_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('UBIGEO', models.CharField(max_length=6)),
                ('ZONA', models.CharField(max_length=5)),
                ('LLAVE_CCPP', models.CharField(max_length=10)),
                ('LLAVE_ZONA', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'TB_ZONA',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='local',
            name='zona',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
