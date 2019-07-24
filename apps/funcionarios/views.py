from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionarios


class FuncionariosList(ListView):
    model = Funcionarios

    def get_queryset(self):
        empresa_logada = self.request.user.funcionarios.empresa
        return Funcionarios.objects.filter(empresa=empresa_logada)


class FuncionariosEdite(UpdateView):
    model = Funcionarios
    fields = ['nome', 'departamentos']


class FuncionariosDelete(DeleteView):
    model = Funcionarios
    success_url = reverse_lazy('list_funcionarios')


class FuncionariosCreate(CreateView):
    model = Funcionarios
    fields = ['nome', 'departamentos']


    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionarios.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)
