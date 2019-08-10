from rest_framework import viewsets
from apps.reg_hora_extra.api.serializers import HoraextraSerializer
from apps.reg_hora_extra.models import Horaextra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class HoraextraViewSet(viewsets.ModelViewSet):
    queryset = Horaextra.objects.all()
    serializer_class = HoraextraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)