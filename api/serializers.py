from rest_framework import serializers
from .models import model_autobus,model_cargador,model_horario,model_programacion_autobuses,model_programacion_cargadores

class autobus_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_autobus
        fields = '__all__'

class horario_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_horario
        fields = '__all__'

class cargador_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_cargador
        fields = '__all__'

class programacion_cargadores_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_programacion_cargadores
        fields = '__all__'

class programacion_autobuses_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_programacion_autobuses
        fields = '__all__'

# Define los otros serializadores de manera similar
