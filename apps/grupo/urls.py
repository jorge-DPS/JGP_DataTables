# -*- coding: utf-8 -*-

from django.urls import path
from django.views.generic.base import TemplateView
from apps.grupo.views.grupo import GrupoListView ,GrupoCreateView,GrupoUpdateView


app_name = 'grupo'
urlpatterns = [
    path('grupolista/', GrupoListView.as_view(), name='lista-grupo'),
    path('formulario/', GrupoCreateView.as_view(), name='crea-grupo'),
    path('editar/<int:codigo_grupo>', GrupoUpdateView.as_view(), name='editar-grupo'),
]
