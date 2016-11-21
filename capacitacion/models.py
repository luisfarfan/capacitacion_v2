from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Ubigeo(models.Model):
    ubigeo = models.CharField(primary_key=True, max_length=6)
    ccdd = models.CharField(max_length=2, blank=True, null=True)
    ccpp = models.CharField(max_length=2, blank=True, null=True)
    ccdi = models.CharField(max_length=2, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MAE_UBIGEO'


class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True, db_column='id_etapa')
    cod_etapa = models.CharField(max_length=3, blank=True, null=True)
    nombre_etapa = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ETAPA'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True, db_column='id_curso')
    cod_curso = models.CharField(max_length=3, blank=True, null=True)
    nombre_curso = models.CharField(max_length=100, blank=True, null=True)
    id_etapa = models.ForeignKey('Etapa', db_column='id_etapa')
    funcionarios = models.ManyToManyField('Funcionario', through='CursoFuncionario')

    class Meta:
        managed = True
        db_table = 'CURSO'


class CursoFuncionario(models.Model):
    id_cursofuncionario = models.AutoField(primary_key=True, db_column='id_cursofuncionario')
    id_funcionario = models.ForeignKey('Funcionario')
    id_curso = models.ForeignKey('Curso')

    class Meta:
        managed = True
        db_table = 'CURSO_FUNCIONARIO'


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True, db_column='id_funcionario')
    cod_funcionario = models.CharField(max_length=3, blank=True, null=True)
    nombre_funcionario = models.CharField(max_length=100, blank=True, null=True)
    id_curso = models.ForeignKey('Curso', db_column='id_curso')

    class Meta:
        managed = True
        db_table = 'FUNCIONARIO'


class Ambiente(models.Model):
    id_ambiente = models.AutoField(primary_key=True, db_column='id_ambiente')
    nombre_ambiente = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'AMBIENTE'


class LocalAmbiente(models.Model):
    id_localambiente = models.AutoField(primary_key=True, db_column='id_localambiente')
    id_local = models.ForeignKey('Local')
    id_ambiente = models.ForeignKey('Ambiente')
    cantidad_disponible = models.IntegerField()
    cantidad_utilizar = models.IntegerField()
    mesas_cant = models.IntegerField(blank=True, null=True)
    sillas_cant = models.IntegerField(blank=True, null=True)
    carpindividuales_cant = models.IntegerField(blank=True, null=True)
    carpbipersonales_cant = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    n_piso = models.IntegerField(blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    puerta_chapa = models.IntegerField(blank=True, null=True)
    puerta_pestillocandado = models.IntegerField(blank=True, null=True)
    puerta_notiene = models.IntegerField(blank=True, null=True)
    sshh = models.IntegerField(blank=True, null=True)
    alumbrado = models.IntegerField(blank=True, null=True)
    pizarra_acrilica = models.IntegerField(blank=True, null=True)
    pizarra_cemento = models.IntegerField(blank=True, null=True)
    proyector = models.IntegerField(blank=True, null=True)
    computadora = models.IntegerField(blank=True, null=True)
    acceso_internet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'LOCAL_AMBIENTE'


class Local(models.Model):
    id_local = models.AutoField(primary_key=True, db_column='id_local')
    ambientes = models.ManyToManyField(Ambiente, through='LocalAmbiente')
    ubigeo = models.ForeignKey(Ubigeo)
    id_curso = models.ForeignKey('Curso')
    nombre_local = models.CharField(max_length=300, blank=True, null=True)
    tipo_via = models.CharField(max_length=300, blank=True, null=True)
    nombre_via = models.CharField(max_length=300, blank=True, null=True)
    referencia = models.CharField(max_length=300, blank=True, null=True)
    n_direccion = models.CharField(max_length=300, blank=True, null=True)
    km_direccion = models.CharField(max_length=300, blank=True, null=True)
    mz_direccion = models.CharField(max_length=300, blank=True, null=True)
    lote_direccion = models.CharField(max_length=300, blank=True, null=True)
    piso_direccion = models.CharField(max_length=300, blank=True, null=True)
    telefono_local_fijo = models.CharField(max_length=10, blank=True, null=True)
    telefono_local_celular = models.CharField(max_length=10, blank=True, null=True)
    fecha_inicio = models.CharField(max_length=100, blank=True, null=True)
    fecha_fin = models.CharField(max_length=100, blank=True, null=True)
    turno_uso_local = models.CharField(max_length=100, blank=True, null=True)
    capacidad_local = models.IntegerField(blank=True, null=True)
    funcionario_nombre = models.CharField(max_length=100, blank=True, null=True)
    funcionario_email = models.CharField(max_length=100, blank=True, null=True)
    funcionario_telefono = models.CharField(max_length=100, blank=True, null=True)
    funcionario_celular = models.CharField(max_length=100, blank=True, null=True)
    responsable_nombre = models.CharField(max_length=100, blank=True, null=True)
    responsable_email = models.CharField(max_length=100, blank=True, null=True)
    responsable_telefono = models.CharField(max_length=100, blank=True, null=True)
    responsable_celular = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'LOCAL'
