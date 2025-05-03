from rest_framework.viewsets import ModelViewSet

from core.models import Marca
from core.serializers.marca import MarcaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all().order_by('id')
    serializer_class = MarcaSerializer
