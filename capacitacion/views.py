from django.http import Http404
from rest_framework.views import APIView
from models import *
from django.db.models import Count
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from serializer import *
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

def modulo_registro(request):
    template = loader.get_template('capacitacion/modulo_registro.html')
    context = {
        'titulo_padre': 'Capacitacion',
        'titulo_hijo': 'REGISTRO DE LOCAL'
    }
    return HttpResponse(template.render(context, request))


def cursos_evaluaciones(request):
    template = loader.get_template('capacitacion/cursos_evaluaciones.html')
    context = {
        'titulo_padre': 'Capacitacion',
        'titulo_hijo': 'Cursos y Evaluaciones'
    }
    return HttpResponse(template.render(context, request))


def asistencia(request):
    template = loader.get_template('capacitacion/asistencia.html')
    context = {
        'titulo_padre': 'Capacitacion',
        'titulo_hijo': 'Modulo de Asistencia'
    }
    return HttpResponse(template.render(context, request))


# Create your views here.

class DepartamentosList(APIView):
    def get(self, request):
        departamentos = list(
            Ubigeo.objects.values('ccdd', 'departamento').annotate(dcount=Count('ccdd', 'departamento')))
        response = JsonResponse(departamentos, safe=False)
        return response


class ProvinciasList(APIView):
    def get(self, request, ccdd):
        provincias = list(
            Ubigeo.objects.filter(ccdd=ccdd).values('ccpp', 'provincia').annotate(dcount=Count('ccpp', 'provincia')))
        response = JsonResponse(provincias, safe=False)
        return response


class DistritosList(APIView):
    def get(self, request, ccdd, ccpp):
        distritos = list(Ubigeo.objects.filter(ccdd=ccdd, ccpp=ccpp).values('ccdi', 'distrito').annotate(
            dcount=Count('ccdi', 'distrito')))
        response = JsonResponse(distritos, safe=False)
        return response


class ZonasList(APIView):
    def get(self, request, ubigeo):
        zonas = list(
            Zona.objects.using('segmentacion').filter(UBIGEO=ubigeo).values('UBIGEO', 'ZONA').annotate(
                dcount=Count('UBIGEO', 'ZONA')))
        response = JsonResponse(zonas, safe=False)
        return response


class TbLocalByUbigeoViewSet(generics.ListAPIView):
    serializer_class = LocalSerializer

    def get_queryset(self):
        ubigeo = self.kwargs['ubigeo']
        return Local.objects.filter(ubigeo=ubigeo)


class TbLocalAmbienteByLocalViewSet(generics.ListAPIView):
    serializer_class = LocalAmbienteSerializer

    def get_queryset(self):
        id_local = self.kwargs['id_local']
        return LocalAmbiente.objects.filter(id_local=id_local)


class LocalAmbienteByLocalAulaViewSet(generics.ListAPIView):
    serializer_class = LocalAmbienteSerializer

    def get_queryset(self):
        id_local = self.kwargs['id_local']
        id_ambiente = self.kwargs['id_ambiente']
        return LocalAmbiente.objects.filter(id_local=id_local, id_ambiente=id_ambiente)


class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class LocalAmbienteViewSet(viewsets.ModelViewSet):
    queryset = LocalAmbiente.objects.all()
    serializer_class = LocalAmbienteSerializer


class CursobyEtapaViewSet(generics.ListAPIView):
    serializer_class = CursoSerializer

    def get_queryset(self):
        id_etapa = self.kwargs['id_etapa']
        return Curso.objects.filter(id_etapa=id_etapa)


class CriteriosViewSet(viewsets.ModelViewSet):
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer


class CursoCriteriosViewSet(viewsets.ModelViewSet):
    queryset = CursoCriterio.objects.all()
    serializer_class = CursoCriterioSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoCriteriobyCursoViewSet(generics.ListAPIView):
    serializer_class = CursoCriterioSerializer

    def get_queryset(self):
        id_curso = self.kwargs['id_curso']
        return CursoCriterio.objects.filter(id_curso=id_curso)


