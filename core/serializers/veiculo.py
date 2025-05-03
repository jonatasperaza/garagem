from rest_framework import serializers

from core.models import Categoria, Cor, Modelo, Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    cor = serializers.PrimaryKeyRelatedField(queryset=Cor.objects.all())
    modelo = serializers.PrimaryKeyRelatedField(queryset=Modelo.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Veiculo
        fields = '__all__'
        read_only_fields = ['id']
