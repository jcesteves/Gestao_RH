from rest_framework import serializers
from apps.funcionarios.models import Funcionarios
from apps.reg_hora_extra.api.serializers import HoraextraSerializer

class FuncionarioSerializer(serializers.ModelSerializer):
    horaextra_set = HoraextraSerializer(many=True)
    class Meta:
        model = Funcionarios
        fields = ['nome', 'user', 'departamentos', 'empresa', 'imagem',
                  'total_hora_extra','horaextra_set']
