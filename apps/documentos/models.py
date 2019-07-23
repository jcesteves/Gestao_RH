from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionarios

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)
    documento = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.pertence.id])