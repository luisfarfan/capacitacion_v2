from rest_framework.views import APIView
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


def distribucion(request):
    template = loader.get_template('capacitacion/distribucion.html')
    context = {
        'titulo_padre': 'Capacitacion',
        'titulo_hijo': 'Modulo de Distribucion'
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
            Zona.objects.using('segmentacion').filter(UBIGEO=ubigeo).values('UBIGEO', 'ZONA', 'ETIQ_ZONA').annotate(
                dcount=Count('UBIGEO', 'ZONA')))
        response = JsonResponse(zonas, safe=False)
        return response


class TbLocalByUbigeoViewSet(generics.ListAPIView):
    serializer_class = LocalSerializer

    def get_queryset(self):
        ubigeo = self.kwargs['ubigeo']
        return Local.objects.filter(ubigeo=ubigeo)


class TbLocalByZonaViewSet(generics.ListAPIView):
    serializer_class = LocalAulasSerializer

    def get_queryset(self):
        ubigeo = self.kwargs['ubigeo']
        zona = self.kwargs['zona']
        return Local.objects.filter(ubigeo=ubigeo, zona=zona)


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


class PEA_BY_AULAViewSet(viewsets.ModelViewSet):
    queryset = LocalAmbiente.objects.all()
    serializer_class = PEA_BY_AULASerializer


@csrf_exempt
def sobrantes_zona(request):
    if request.method == "POST" and request.is_ajax():
        ubigeo = request.POST['ubigeo']
        zona = request.POST['zona']
        sobrantes = PEA.objects.exclude(id_pea__in=PEA_AULA.objects.values('id_pea')).filter(ubigeo=ubigeo,
                                                                                             zona=zona).order_by(
            'ape_paterno').values('dni', 'ape_paterno', 'ape_materno', 'nombre', 'cargo')
        return JsonResponse(list(sobrantes), safe=False)

    return JsonResponse({'msg': False})


@csrf_exempt
def asignar(request):
    if request.method == "POST" and request.is_ajax():
        ubigeo = request.POST['ubigeo']
        zona = request.POST['zona']
        locales_zona = Local.objects.filter(ubigeo=ubigeo, zona=zona)
        for e in locales_zona:
            aulas_by_local = LocalAmbiente.objects.filter(id_local=e.id_local)
            for a in aulas_by_local:
                if disponibilidad_aula(a.id_localambiente):
                    pea_ubicar = PEA.objects.exclude(id_pea__in=PEA_AULA.objects.values('id_pea')).filter(ubigeo=ubigeo,
                                                                                                          zona=zona).order_by(
                        'ape_paterno')[:a.capacidad]
                    for p in pea_ubicar:
                        pea = PEA.objects.get(pk=p.id_pea)
                        aula = LocalAmbiente.objects.get(pk=a.id_localambiente)
                        pea_aula = PEA_AULA(id_pea=pea, id_localambiente=aula)
                        pea_aula.save()

        return JsonResponse({'msg': True})

    return JsonResponse({'msg': False})


def disponibilidad_aula(aula):
    aula = LocalAmbiente.objects.get(pk=aula)
    cantidad_asignada = PEA_AULA.objects.filter(id_localambiente=aula).count()
    is_disponible = True

    if cantidad_asignada >= aula.capacidad:
        is_disponible = False

    return is_disponible
