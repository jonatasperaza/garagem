from rest_framework import serializers

from core.models import Modelo


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
        read_only_fields = ['id']
