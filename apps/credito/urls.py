from django.urls import path
from django.views.generic.base import TemplateView
from apps.cajas.views.caja import (CajaListView,CajaView, CajaImprimirView)
#from apps.cajas.views.reportecaja import CajaReporte
#from apps.cajas.reports.reportecaja import CajaReporte
from apps.clientes.reports.reporte_ficha_datos import FichaDatos

from apps.credito.reports.rep_liquidacion import ReporteLiquidacionPrestamo
from apps.credito.reports.reporte_rutas import ReporteRutas,ReporteRutas_excel
from apps.credito.reports.rep_condonacion import ReporteCondonaciones
from apps.credito.reports.rep_depositos_aplicados import ReporteCreditoAplicados
from apps.credito.reports.rep_historial_prestamos import HistorialPrestamos

from apps.credito.reports.rep_excel import Convertidor
#datatables
from django.conf.urls import url, include
from rest_framework import routers
from apps.credito.views import views

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
#------------

app_name = 'credito'
urlpatterns = [
    #***datatables
    url('^api/', include(router.urls)),
    url('datatables/', views.index, name='albums'),
    path(
        'api/post-list/albums/',
        views.AlbumPostListView.as_view(),
        name='albums_post_list'
    ),
    path(
        'api/filter/albums/artist/options/',
        views.AlbumFilterArtistOptionsListView.as_view(),
        name='albums_filter_artist_options_list'
    ),
    path(
        'api/filter/albums/',
        views.AlbumFilterListView.as_view(),
        name='albums_filter_list'
    ),
    path('', views.index, name='albums'),
    #*******
    path(
        'liquidacion/',
        ReporteLiquidacionPrestamo.as_view(),
        name="pdf-liquidacion"
    ),
    path(
        'rutas/',
        ReporteRutas.as_view(),
        name="pdf-rutas"
    ),
    path(
        'rutas_excel/',
        ReporteRutas_excel.as_view(
            {'get':'excel'}
        ),
        name="excel-rutas"
    ),
    path(
        'condonacion/',
        ReporteCondonaciones.as_view(),
        name="pdf-condonacion"
    ),
    path(
        'depositos_aplicados/inicial=<str:fecha_inicio>/<str:hora_inicio>/final=<str:fecha_fin>/<str:hora_fin>',
        ReporteCreditoAplicados.as_view(),
        name="pdf-creditos-aplicados"
    ),
    
    path(
        'historial_prestamos/',
        HistorialPrestamos.as_view(),
        name="pdf-prestamos"
    ),
    #converti a excel
    path(
        'convertirexcel/',
        Convertidor.as_view(),
        name="excel-ruta"
    ),
    
    
    
]    
