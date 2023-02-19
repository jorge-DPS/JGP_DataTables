from django.urls import path
from apps.administracion.api.v1.views.persona import (PersonaViewSet,PersonaCreateViewSet,
                                        PersonaDeleteViewSet, PersonaEditViewSet,PersonaList)

app_name = 'api-administracion'
urlpatterns = [
    #PERSONAS
    path(
        'personas/',
        PersonaViewSet.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='personas-lista',
    ),
    path(
        'personas/<int:pk>/',
        PersonaEditViewSet.as_view(
            {'get': 'get', 'put': 'update', 'post' : 'delete'}
        ),
        name='get-deposito',
    ),
    path(
        'personas/list/',
        PersonaList.as_view(
            {'get': 'listar'}
        ),
        name='listar-persona'
    ),    
    #RUTAS
   
]                                     
