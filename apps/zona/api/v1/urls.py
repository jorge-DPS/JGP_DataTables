# -*- coding: utf-8 -*-

from django.urls import path

from apps.zona.api.v1.views.zona import (ZonaViewSet, ZonasViewSet)
from apps.zona.api.v1.views.localidad import (LocalidadCRUD, FilterLocalidad,DatatablesLocalidad)

app_name = 'zona'
urlpatterns = [
    # >> Ubicacion 
    #listar, crear zona
    path('zonas/',ZonaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }),
    name="lista-crea"),
    #lista, edita,elimina zona
    path('zona/<int:id>',ZonasViewSet.as_view({
        'get': 'retrieve',
        'put':'update',
        'delete':'delete'
    }),
    name="list-edita-elimina"),
   
    # >> Localidad 
    #listar localidad
    path('localidad/',LocalidadCRUD.as_view({
        'get': 'list',
        'post': 'create',
    }),
    name="list-localidad"),
    #detalle localidad
    path('localidad/<int:id>/',LocalidadCRUD.as_view({
        'get': 'retrive',
        'put':'update',
        'delete':'delete'
    }),
    name="detalle-localidad"),
    
    path('localidad',FilterLocalidad.as_view(),name="filtrar-localidad"),
#--------datatables
    path('localidad_datatables',DatatablesLocalidad.as_view(),name="lista-datables"),
]