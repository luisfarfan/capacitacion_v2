# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0014_auto_20161128_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PEA',
            fields=[
                ('id_pea', models.AutoField(db_column='id_pea', primary_key=True, serialize=False)),
                ('id_per', models.CharField(blank=True, max_length=8, null=True)),
                ('dni', models.CharField(blank=True, max_length=8, null=True)),
                ('ape_paterno', models.CharField(blank=True, db_column='ape_paterno', max_length=100, null=True)),
                ('ape_materno', models.CharField(blank=True, db_column='ape_materno', max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=100, null=True)),
                ('id_cargofuncional', models.IntegerField(db_column='id_cargofuncional')),
                ('cargo', models.CharField(blank=True, db_column='cargo', max_length=50, null=True)),
                ('ubigeo', models.ForeignKey(db_column='ubigeo', on_delete=django.db.models.deletion.CASCADE, to='capacitacion.Ubigeo')),
            ],
            options={
                'db_table': 'PEA',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PEA_AULA',
            fields=[
                ('id_peaaula', models.AutoField(db_column='id_peaaula', primary_key=True, serialize=False)),
                ('id_localambiente', models.ForeignKey(db_column='id_localambiente', on_delete=django.db.models.deletion.CASCADE, to='capacitacion.LocalAmbiente')),
                ('id_pea', models.ForeignKey(db_column='id_pea', on_delete=django.db.models.deletion.CASCADE, to='capacitacion.PEA')),
            ],
        ),
        migrations.AddField(
            model_name='localambiente',
            name='pea',
            field=models.ManyToManyField(through='capacitacion.PEA_AULA', to='capacitacion.PEA'),
        ),
    ]
