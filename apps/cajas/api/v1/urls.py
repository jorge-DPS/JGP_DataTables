from django.urls import path
from apps.cajas.api.v1.views.caja import (CajaViewSet,CajaEditViewSet)
from apps.cajas.api.v1.views.arqueo import (
                                            DetalleArqueoView,
                                            ArqueoViewSet,
                                            ArqueoEditView,
                                            CuentasPorCobrarViewSet,
                                            CuentaPorCobrarViewSet,
                                            TransaccionInventariosViewSet,
                                            TransaccionInventarioViewSet,
                                            InventarioViewSet,
                                            ArqueoCajaView,
                                            FilterArqueoCaja,
                                            FilterUsuario,
                                            get_jasper 
                                        
                                            )
from apps.cajas.api.v1.views.corte_moneda import (FilterCorteMoneda,CortesViewSet, CorteViewSet)

app_name = 'api-cajas'

urlpatterns = [
    #============================Cajas=================
    path(
        'cajas/',
        CajaViewSet.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='cajas-lista-crear',
    ),
    path(
        'caja/<int:pk>',
        CajaEditViewSet.as_view(
            {'delete': 'delete','get': 'retrieve','put': 'update'}
        ),
        name='cajas-eliminar-editar',
    ),
    #============================Arqueos=================
    path(
        'arqueos/',
        ArqueoViewSet.as_view(
            {'get':'list','post':'create'}
        ),
        name='arqueo-lista-crear',
    ),
    path(
        'arqueo/<int:pk>',
        ArqueoEditView.as_view(
            {'delete': 'delete','get': 'retrieve','put': 'update'}
        ),
        name='cajas-eliminar-editar',
    ),
    path(
        'arqueo_detalle/<int:pk>',
        DetalleArqueoView.as_view(
            {'get': 'lista'}
        ),
        name='detalles-arqueo',
    ),
    #============================Arqueos detalle INVENTARIO CUENTAS=================
    path(
        'arqueo/<int:pk>',
        ArqueoEditView.as_view(
            {'delete': 'delete','get': 'retrieve','put': 'update'}
        ),
        name='cajas-eliminar-editar',
    ),
#============================Arqueos detalle INVENTARIO CUENTAS=================
    #============================Corte Moneda=================
    #crear,listar corte_moneda
    path('corte_monedas/',CortesViewSet.as_view({
        'post': 'create',
        'get': 'list',
    }),
    name='corte_moneda-crear-listar'),
    #listar un registro corte_moneda
    path('corte_moneda/<int:id>',CorteViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'delete'
    }),
    name="corte_moneda-detalle-edita-elimina"),
    #filtrar corte moneda list_moneda en filtrados
    path('corte_moneda',FilterCorteMoneda.as_view(),name="filtrar-moneda"),
    
    #============================Cuentas por Cobrar=================
    path('cuentas_cobrar/',CuentasPorCobrarViewSet.as_view({
        'post': 'create',
        'get': 'list',
    }),
    name='cuenta-cobrar-crear-listar'),
    #listar un registro cuenta-cobrar
    path('cuentas_cobrar/<int:id>',CuentaPorCobrarViewSet.as_view({
        'get':'retrieve',
        'put':'cobros',
        'delete':'delete'
    }),
    name="cuenta-cobrar-detalle-edita-elimina"),
    
    #listar un registro cuenta-cobrar para jasper
   
    #============================Transacciones Inventarios=================
    path('transaccion_inventarios/',TransaccionInventariosViewSet.as_view({
        'post': 'create',
        'get': 'list_api',
    }),
    name='transaccion-inventario-crear-listar'),
    #listar un registro transaccion-inventario
    path('transaccion_inventarios/<int:id>',TransaccionInventarioViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'delete'
    }),
    name="transaccion-inventario-detalle-edita-elimina"),
    
    #listar transaccion-inventario para jasper
    path('inventario_mercaderia/',InventarioViewSet.as_view({
        'get':'list'
    }),
    name="inventario-mercaderia"),
    
    
  #=========================ARQUEO INVENARIO CUENTAS===================================
    path('arqueo_caja/<int:pk>/<str:fecha>',ArqueoCajaView.as_view({
        'get':'retrieve'
    }),
    name="transaccion-inventario-arqueo"),
    

#=========================ARQUEO INVENARIO CUENTAS===================================
    path('arqueo_caja',FilterArqueoCaja.as_view(),name="filter-transaccion-inventario-arqueo"),

#=========================ARQUEO INVENARIO CUENTAS===================================
    path('usuario',FilterUsuario.as_view(),name="filter-usuario"),
    
    
#============================API PARA JASPER=================
    path(
        'prueba/',
        get_jasper.as_view(
            {'get': 'list', 'post': 'create'}
        ),
        name='cajas-lista-crear',
    ),
    
]    
