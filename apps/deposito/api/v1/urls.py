from django.urls import path

from apps.deposito.api.v1.views.deposito import (DepositosViewSet, DepositoViewSet)

app_name = 'deposito'
urlpatterns = [
    # >> Deposito  
    #crear,listar deposito
    path('extracto-depositos/',DepositosViewSet.as_view({
        'post': 'save_array_deposito',
        'get': 'list',
    }),
    name='deposito-crear-listar'),
    
    #listar un registro deposito
    path('extracto-deposito/<int:id>',DepositoViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'delete'
    }),
    name="deposito-detalle-edita-elimina"),

]

