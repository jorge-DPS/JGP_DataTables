from django.urls import path
from django.views.generic.base import TemplateView
from apps.cajas.views.caja import (CajaListView,CajaView, CajaImprimirView)
#from apps.cajas.views.reportecaja import CajaReporte
from apps.cajas.reports.reportecaja import CajaReporte

app_name = 'cajas'
urlpatterns = [
    path(
        'cajas/',
        CajaListView.as_view(),
        name="lista-cajas"
    ),
    path(
        'cajas/nuevo/',
        CajaView.as_view(),
        name="nuevo-caja"
    ),
    path(
        'cajas/reporte',
        CajaImprimirView.as_view(),
        name="pdf-caja"
    ),
    
    path(
        'cajaspdf/<int:pk>/<str:fecha>',
        CajaReporte.as_view(),
        name="pdf-cajaarqueo"
    ),
]    
