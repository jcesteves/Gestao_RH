from django.urls import path
from .views import EmpresaCreate, EmpresaEdite

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='empresacreate'),
    path('edit/<int:pk>', EmpresaEdite.as_view(), name='empresaedit'),

]
