from rest_framework import serializers
from apps.reg_hora_extra.models import Horaextra

class HoraextraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaextra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']
