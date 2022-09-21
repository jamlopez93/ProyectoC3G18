from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, views
from urllib import request

from authApp.models.paciente import Paciente
from authApp.serializers.pacienteSerializer import PacienteSerializer

class VistaDetallePaciente(APIView):
    def get_object(self, pk):
        try:
            return Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)
