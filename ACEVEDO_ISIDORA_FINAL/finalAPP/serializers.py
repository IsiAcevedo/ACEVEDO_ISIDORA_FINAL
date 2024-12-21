from rest_framework import serializers
from .models import *

class ParticipanteSerializer(serializers.ModelSerializer):
    institucion_nombre = serializers.ReadOnlyField(source='institucion.nombre')

    class Meta:
        model = Participante
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'