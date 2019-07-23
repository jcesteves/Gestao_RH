from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreate.as_view(), name='documento_create'),
    #path('edit/<int:pk>', EmpresaEdite.as_view(), name='empresaedit'),

]
