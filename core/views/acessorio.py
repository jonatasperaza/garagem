from rest_framework.viewsets import ModelViewSet
from core.serializers.acessorio import AcessorioSerializer
from core.models import Acessorio


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all().order_by('id')
    serializer_class = AcessorioSerializer

