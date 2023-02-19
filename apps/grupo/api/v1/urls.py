from django.urls import path

from apps.grupo.api.v1.views.grupo import (GruposViewSet, GrupoViewSet)

app_name = 'grupo'
urlpatterns = [
    # >> Grupo solidario 
    #crear,listar grupo
    path('grupos/',GruposViewSet.as_view({
        'post': 'create',
        'get': 'list',
    }),
    name='grupo-crear-listar'),
    
    #listar un registro grupo
    path('grupo/<int:codigo_grupo>',GrupoViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'delete'
    }),
    name="grupo-detalle-edita-elimina"),

]

