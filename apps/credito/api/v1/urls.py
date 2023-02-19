from django.urls import path
from apps.credito.api.v1.views.credito import (EvaluacionesEconimincaViewSet,
                                            EvaluacionEconimincaViewSet
                                              
                                            )

app_name = 'credito'

urlpatterns = [
    
    #============================Evaluacion economica=================
    path(
        'evaluaciones/',
        EvaluacionesEconimincaViewSet.as_view(
            {'get':'list','post':'create'}
        ),
        name='arqueo-lista-crear',
    ),
    path(
        'evaluacion/<int:pk>',
        EvaluacionEconimincaViewSet.as_view(
            {'delete': 'delete','get': 'retrieve','put': 'update'}
        ),
        name='credito-eliminar-editar',
    ),
    

  

]    
