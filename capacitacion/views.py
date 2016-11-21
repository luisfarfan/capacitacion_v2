from django.http import Http404
from rest_framework.views import APIView
from models import *
from django.db.models import Count
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from serializer import *
from rest_framework import generics


def gato(request):
    template = loader.get_template('capacitacion.html')
    context = {
        'gatos': '',
        'title': ''
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


class TbLocalByUbigeoViewSet(generics.ListAPIView):
    serializer_class = LocalSerializer

    def get_queryset(self):
        ubigeo = self.kwargs['ubigeo']
        return Local.objects.filter(ubigeo=ubigeo)


class TbLocalAmbienteByUbigeoViewSet(generics.ListAPIView):
    serializer_class = LocalAmbienteSerializer

    def get_queryset(self):
        id_local = self.kwargs['id_local']
        return Local.objects.filter(id_local=id_local)


class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class LocalAmbienteViewSet(viewsets.ModelViewSet):
    queryset = LocalAmbiente.objects.all()
    serializer_class = LocalAmbienteSerializer
