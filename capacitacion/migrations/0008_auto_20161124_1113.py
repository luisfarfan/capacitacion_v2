# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0007_auto_20161122_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id_criterio', models.AutoField(db_column='id_criterio', primary_key=True, serialize=False)),
                ('nombre_criterio', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_criterio', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'CRITERIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CursoCriterio',
            fields=[
                ('id_cursocriterio', models.AutoField(db_column='id_cursocriterio', primary_key=True, serialize=False)),
                ('descripcion_criterio', models.CharField(blank=True, max_length=100, null=True)),
                ('peso', models.IntegerField()),
                ('id_criterio', models.ForeignKey(db_column='id_criterio', on_delete=django.db.models.deletion.CASCADE, to='capacitacion.Criterio')),
            ],
            options={
                'db_table': 'CURSO_CRITERIO',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='nota_minima',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cursocriterio',
            name='id_curso',
            field=models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, to='capacitacion.Curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='criterios',
            field=models.ManyToManyField(through='capacitacion.CursoCriterio', to='capacitacion.Criterio'),
        ),
    ]
