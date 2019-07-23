from django.forms import ModelForm
from apps.funcionarios.models import Funcionarios
from .models import Horaextra


class Horaextraforms(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(Horaextraforms, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionarios.objects.filter(empresa=user.funcionarios.empresa)

    class Meta:
        model = Horaextra
        fields = ['motivo', 'funcionario', 'horas']
