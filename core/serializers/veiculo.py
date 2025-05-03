from rest_framework import serializers

from core.models import Categoria, Cor, Marca, Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    cor = serializers.PrimaryKeyRelatedField(queryset=Cor.objects.all())
    marca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Veiculo
        fields = '__all__'
        read_only_fields = ['id']
