import json
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views import View
from apps.reg_hora_extra.forms import Horaextraforms
from .models import Horaextra


class HoraExtra(ListView):
    model = Horaextra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionarios.empresa
        return Horaextra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdite(UpdateView):
    model = Horaextra
    fields = ['motivo', 'funcionario', 'horas']

    # def get_form_kwargs(self):
    #     kwargs = super(HoraExtraEdite, self).get_form_kwargs()
    #     kwargs.update({'user': self.request.user})
    #     return kwargs


class HoraExtraDelete(DeleteView):
    model = Horaextra
    success_url = reverse_lazy('list_horaextra')


class HoraExtraCreate(CreateView):
    model = Horaextra
    form_class = Horaextraforms

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

#Regra de negócio - Debitando Hora Extra
class utilizouhoraextra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = Horaextra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        empregado = self.request.user.funcionarios
        
        response = json.dumps({'mensagem': 'tudo certo', 'Horas': float(empregado.total_hora_extra)})
        return HttpResponse(response, content_type='application/json')


class naousouhoraextra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = Horaextra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        empregado = self.request.user.funcionarios
        
        response = json.dumps({'mensagem': 'tudo certo', 'Horas': float(empregado.total_hora_extra)})
        return HttpResponse(response, content_type='application/json')