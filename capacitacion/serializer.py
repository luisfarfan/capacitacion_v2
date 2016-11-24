from .models import *
from rest_framework import routers, serializers, viewsets


class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local


class LocalAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalAmbiente


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso


class CriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterio


class CursoCriterioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoCriterio
