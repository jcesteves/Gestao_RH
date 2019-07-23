from django.urls import path
from .views import FuncionariosList, FuncionariosEdite, FuncionariosDelete, FuncionariosCreate

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionariosCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', FuncionariosEdite.as_view(), name='update_funcionario'),
    path('excluir/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionario')

]
