from django.urls import path
from django.views.generic.base import TemplateView
from apps.administracion.views.persona import (PersonaListView,PersonaCreateView, PersonaReporteView,PersonaDetalleView,PersonaEditarView)

#PERSONAS
app_name = 'administracion'
urlpatterns = [
    path(
        'personas/',
        PersonaListView.as_view(),
        name="lista-persona"
    ),
    path(
        'personas/nuevo/',
        PersonaCreateView.as_view(),
        name="nuevo-persona"
    ),
    path(
        'persona/reporte/<int:pk>/',
        PersonaReporteView.as_view(),
        name="pdf-persona"
    ),
    path(
        'persona/detalle/<int:pk>/',
        PersonaDetalleView.as_view(),
        name="persona-detalle"
    ),
    path(
        'persona/editar/<int:pk>/',
        PersonaEditarView.as_view(),
        name="persona-editar"
    ),
    
   
]
