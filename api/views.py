from django.shortcuts import render
from rest_framework import generics
from .models import model_autobus,model_cargador,model_horario,model_programacion_autobuses,model_programacion_cargadores
from .serializers import programacion_autobuses_serializer,programacion_cargadores_serializer , cargador_serializer, autobus_serializer, horario_serializer

class AutobusListCreate(generics.ListCreateAPIView):
    queryset = model_autobus.objects.all()
    serializer_class = autobus_serializer

class AutobusRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_autobus.objects.all()
    serializer_class = autobus_serializer

class HorarioListCreate(generics.ListCreateAPIView):
    queryset = model_horario.objects.all()
    serializer_class = horario_serializer

class HorarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_horario.objects.all()
    serializer_class = horario_serializer

class ProgramacionAutobusesListCreate(generics.ListCreateAPIView):
    queryset = model_programacion_autobuses.objects.all()
    serializer_class = programacion_autobuses_serializer

class ProgramacionAutobusesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_programacion_autobuses.objects.all()
    serializer_class = programacion_autobuses_serializer

class CargadorListCreate(generics.ListCreateAPIView):
    queryset = model_cargador.objects.all()
    serializer_class = cargador_serializer

class CargadorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_cargador.objects.all()
    serializer_class = cargador_serializer

class ProgramacionCargadoresListCreate(generics.ListCreateAPIView):
    queryset = model_programacion_cargadores.objects.all()
    serializer_class = programacion_cargadores_serializer

class ProgramacionCargadoresRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_programacion_cargadores.objects.all()
    serializer_class = programacion_cargadores_serializer