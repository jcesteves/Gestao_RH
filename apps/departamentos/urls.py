from django.urls import path
from .views import DepartamentosList, DepartamentosCreate, DepartamentosUpdate, DepartamentosDelete

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentosCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentosUpdate.as_view(), name='update_departamento'),
    path('excluir/<int:pk>', DepartamentosDelete.as_view(), name='delete_departamento'),
]
