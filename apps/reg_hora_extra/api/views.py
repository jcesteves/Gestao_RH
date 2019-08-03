from rest_framework import viewsets
from apps.reg_hora_extra.api.serializers import HoraextraSerializer
from apps.reg_hora_extra.models import Horaextra


class HoraextraViewSet(viewsets.ModelViewSet):
    queryset = Horaextra.objects.all()
    serializer_class = HoraextraSerializer
    