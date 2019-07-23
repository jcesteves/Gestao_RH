from django.urls import path
from .views import HoraExtra, HoraExtraEdite, HoraExtraDelete, HoraExtraCreate, utilizouhoraextra

urlpatterns = [
    path('', HoraExtra.as_view(), name='list_horaextra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_horaextra'),
    path('editar/<int:pk>', HoraExtraEdite.as_view(), name='update_horaextra'),
    path('utilizou/<int:pk>/', utilizouhoraextra.as_view(), name='utilizou_horaextra'),
    path('delete/<int:pk>', HoraExtraDelete.as_view(), name='delete_horaextra'),
]
