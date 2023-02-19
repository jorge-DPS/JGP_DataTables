from django.urls import path
from apps.procesos.arqueo.api.v1.views.caja import (CajaViewSet,CajaCreateViewSet,CajaDeleteViewSet)

app_name = 'caja'
urlpatterns = [
    path(
        'cajas/',
        CajaViewSet.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='caja-lista',
    ),
    path(
        'cajas/crear/',
        CajaCreateViewSet.as_view({'post': 'create'} ),
        name='caja-lista',
    ),
    path(
        'caja/delete/<int:pk>/',
        CajaDeleteViewSet.as_view(
            {'put': 'delete'}
        ),
        name='get-caja',
    ),
]
