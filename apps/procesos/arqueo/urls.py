from django.urls import path
from django.views.generic.base import TemplateView

from apps.procesos.arqueo.views.caja import (CajaListView,CajaCreateView,CajaDetalleView,CajaImprimirView)


app_name = 'cajas'
urlpatterns = [
    path(
        'caja/',
        CajaListView.as_view(),
        name="lista-caja"
    ),
    path(
        'caja/nuevo/',
        CajaCreateView.as_view(),
        name="nuevo-caja"
    ),
    path(
        'caja/detalle/<int:pk>/',
        CajaDetalleView.as_view(),
        name="pdf-detalle"
    ),
    path(
        'caja/reporte/<int:pk>/',
        CajaImprimirView.as_view(),
        name="pdf-contrato"
    ),
]
