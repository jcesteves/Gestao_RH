from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionarios


class Horaextra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('list_horaextra')
