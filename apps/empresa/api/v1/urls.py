# -*- coding: utf-8 -*-

from django.urls import path

from apps.empresa.api.v1.views.sucursal import (SucursalListView)

app_name = 'empresa'
urlpatterns = [
    # >> Sucursales
    
    path(
        'empresa/sucursales/',
        SucursalListView.as_view({'get': 'list'}),
        name="list-sucursales"
    ),
]
