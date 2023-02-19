from django.urls import path
from django.views.generic.base import TemplateView
from apps.cajas.views.caja import (CajaListView,CajaView, CajaImprimirView)
#from apps.cajas.views.reportecaja import CajaReporte
#from apps.cajas.reports.reportecaja import CajaReporte
from apps.clientes.reports.reporte_ficha_datos import FichaDatos

app_name = 'clientes'
urlpatterns = [
    
    path(
        'ficha_datos/',
        FichaDatos.as_view(),
        name="pdf-cajaarqueo"
    ),
]    
