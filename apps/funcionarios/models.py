from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.db.models import Sum

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT,
                                blank=True, null=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    @property
    def total_hora_extra(self):
        total = self.horaextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return total

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Funcionarios'
