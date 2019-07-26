from rest_framework import serializers
from apps.funcionarios.models import Funcionarios

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'user', 'departamentos', 'empresa', 'imagem']
