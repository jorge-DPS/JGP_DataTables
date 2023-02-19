import decimal
from os import stat
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from apps.accounts.api.v1 import serializers
from apps.contrib.api.viewsets import ModelCreateListViewSet, ModelUpdateListViewSet, ModelRetrieveUpdateListViewSet
from apps.contrib.api.exceptions import NotFound
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.cajas.models.caja import Caja 
from apps.accounts.models import User
from apps.cajas.models.arqueo import EncabezadoArqueo,DetalleArqueo,CuentasPorCobrar, TransaccionInventario
from apps.contrib.api.viewsets import ModelCreateListViewSet
from apps.contrib.api.viewsets import PermissionViewSet
from apps.contrib.api.viewsets import (ModelCreateListViewSet, 
                                        ModelRetrieveUpdateListViewSet, PermissionlMixin)
from datetime import datetime
from apps.cajas.api.v1.serializers.arqueo import (DetalleArqueoSerializer,
                                                  EncabezadoArqueoSerializer,
                                                  EncabezaJnSerializer,
                                                  CuentasPorCobrarSerializer,
                                                  CuentasPorCobrarListarSerializer,
                                                  TransaccionInventarioSerializer,
                                                  TransaccionInventarioListarSerializer,
                                                  EncabezadoArqueoPOSTSerializer,
                                                  #CuentasPorCobrarUsuarioSerializer,
                                                  ArqueoCajaSerializer,
                                                  ActualizadoEncabezado,ActualizadoInventario,
                                                  UserUpdateSerializer,
                                                  CuentasPorCobrarListarGETSerializer
                                                  )
from rest_framework import filters
from rest_framework import generics

class LogMixin(object):
    def load_logs(self):
        data=self.request.data
        data['usuario_actualizacion']=self.request.user.pk
        data['sucursal_creacion']=self.request.user.branch_office.pk
        return data
    def now_fecha(self):
        tiempo = datetime.now()
        fechahora = tiempo.replace(microsecond=0)
        #fechahora = tiempo.strftime("%Y/%m/%d %H:%M:%S")
        data=fechahora
        return data
    
    def caja(self):
        data=self.request.data
        data['usuario_id']=self.request.user.pk
        codeUser=User.objects.get(id=data['usuario_id'])
        dataCaja=Caja.objects.get(codigo_usuario=codeUser.pk)
        dato=dataCaja.pk
        return dato
        
    def user(self):
        data=self.request.data
        data=self.request.user.pk
        return data
        
#==================================Encabezdo Arqueo==========================   
class ArqueoViewSet(PermissionViewSet, ModelCreateListViewSet,LogMixin):
    """Contains all persona endpoints."""
    serializer_class = EncabezadoArqueoSerializer
    #permission_classes = [IsAuthenticated]
    #permission_denied_message = 'no esta autorizado'
    def get_queryset(self):
        queryset = EncabezadoArqueo.objects.filter(arqueo_definitivo=False)
        return queryset
    
    def list(self, request, *args, **kwargs):
        arqueo = EncabezadoArqueo.objects.filter(arqueo_definitivo=True).order_by('-id')
        return Response(self.get_serializer(arqueo, many=True).data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        data=request.data
        print("========datos de post===",data)
        data['caja_id']=self.caja()
        data['usuario_id']=self.user()
        data=self.load_logs()
        data['fecha_arqueo']=self.now_fecha()
        data['creado_en']=self.now_fecha()
        encabezado_serializer=EncabezadoArqueoPOSTSerializer(data=data)
        encabezado_serializer.is_valid(raise_exception=True)
        encabezado=encabezado_serializer.create(encabezado_serializer._validated_data)
        data_arqueo=data['detalle_arqueo_encabezado']
        #del data['detalle_arqueo_encabezado']
        if request.data["detalle_arqueo_encabezado"]:
            for detalle in data_arqueo:
                detalle['arqueo_id']=encabezado.id
                detalle['usuario_actualizacion']=self.request.user.pk
                detalle['sucursal_creacion']=self.request.user.branch_office.pk
                detalle['creado_en']=self.now_fecha()
                self.create_detalle_arqueo(detalle)
            return Response({'messaje':'Se registro corectamente'},status=status.HTTP_201_CREATED)
        else:
            data_error={
                "message":"Registre uno o mas detalles"
            }
            return Response(data_error,status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def create_detalle_arqueo(self,data):
        serializer=DetalleArqueoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        detalle_arqueo=serializer.create(serializer.validated_data)
        return detalle_arqueo
        

#=========================ARQUEO INVENTARIO CUENTAS
class ArqueoCaja(ArqueoViewSet,IsAuthenticated, ModelRetrieveUpdateListViewSet,LogMixin):
    arqueo_detail=ArqueoCajaSerializer 
    def get_queryset(self):
        return EncabezadoArqueo.objects.all()
 
    def retrieve(self, request, *args, **kwargs):
        
        arqueo_detalle = EncabezadoArqueo.objects.get(id=kwargs["pk"])
        if(arqueo_detalle.eliminado_en is None):
            detalle_serializer=self.arqueo_detail(arqueo_detalle)
            return Response(detalle_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"Este registro esta eliminado"})

   
class ArqueoEditView(ArqueoViewSet,IsAuthenticated, ModelRetrieveUpdateListViewSet,LogMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = EncabezadoArqueoSerializer
    arqueo_detail=EncabezaJnSerializer 
    #permission_denied_message = 'no esta autorizado'
    def get_queryset(self):
        return EncabezadoArqueo.objects.all()
    
    def update(self, request, *args, **kwargs):
        print("========datos de put===",kwargs["pk"])
        arqueo=EncabezadoArqueo.objects.get(id=kwargs["pk"])
        data=self.request.data
        #data_arqueo=data['detalle']
        #del data['detalle']
        arqueo.arqueo_definitivo=False
        arqueo.actualizado_en=self.now_fecha()
        serializer = EncabezadoArqueoSerializer(arqueo,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("================almacenado final",serializer)
        data=request.data
        print("========datos de post nuevo===",data)
        data_arqueo=data['detalle_arqueo_encabezado']
        del data['detalle_arqueo_encabezado']
        data['caja_id']=self.caja()
        data['usuario_id']=self.user()
        data=self.load_logs()
        data['fecha_arqueo']=self.now_fecha()
        data['creado_en']=self.now_fecha()
        encabezado_serializer=EncabezadoArqueoPOSTSerializer(data=data)
        encabezado_serializer.is_valid(raise_exception=True)
        encabezado=encabezado_serializer.create(encabezado_serializer._validated_data)
        print("================almacenado final",encabezado)
        for detalle in data_arqueo:
            detalle['arqueo_id']=encabezado.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_detalle_arqueo(detalle)            
           # return Response({'messaje':'Guardado'},status=status.HTTP_201_CREATED)
        return Response({'messaje':'Guardado los cambios'},status=status.HTTP_201_CREATED)

    def create_detalle_arqueo(self,data):
        print("======post detelle de arqueo")
        serializer=DetalleArqueoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        detalle_arqueo=serializer.create(serializer.validated_data)
        return detalle_arqueo
        
    def retrieve(self, request, *args, **kwargs):
        
        arqueo_detalle = EncabezadoArqueo.objects.get(id=kwargs["pk"])
        if(arqueo_detalle.eliminado_en is None):
            detalle_serializer=self.arqueo_detail(arqueo_detalle)
            return Response(detalle_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"Este registro esta eliminado"})

    def delete (self, request, *args, **kwargs):
        try:
            print("******************** Eliminando Arqueo: ", kwargs["pk"])
            arqueo = EncabezadoArqueo.objects.get(pk=kwargs["pk"])
            #arqueo.estado_arqueo = "B"
            detalle=DetalleArqueo.objects.filter(arqueo_id=kwargs["pk"])
            for datos in detalle:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            arqueo.arqueo_definitivo=False
            arqueo.eliminado_en=self.now_fecha()
            arqueo.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({'message':'No existe el registro '},status=status.HTTP_406_NOT_ACCEPTABLE)
    
#==================================Detalles de los Arques==========================   
class DetalleArqueoView(IsAuthenticated, ModelRetrieveUpdateListViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EncabezaJnSerializer 
    model=DetalleArqueo
    queryset = EncabezadoArqueo.objects.all()
    
    def lista(self, request, *args, **kwargs):
        print("Detalles del id :============== ",kwargs["pk"])
        arqueo_detalle = EncabezadoArqueo.objects.get(id=kwargs["pk"])
        detalle_serializer=self.serializer_class(arqueo_detalle)
        return Response(detalle_serializer.data, status=status.HTTP_200_OK)

#==================================Cuentas por Cobrar  para jasper==========================  

#==================================Cuentas por Cobrar==========================  
class CuentasPorCobrarViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = CuentasPorCobrarSerializer
    lista_corte_moneda= CuentasPorCobrarListarGETSerializer
    
    def list(self, request, *args, **kwargs):
        cuenta_cobrar = CuentasPorCobrar.objects.filter(eliminado_en=None).order_by('-id')
        return Response(self.lista_corte_moneda(cuenta_cobrar, many=True).data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = CuentasPorCobrar.objects.filter(eliminado_en=None)   
        return queryset
    
    def create(self, request, *args, **kwargs):
        try:
            #data._mutable=True
            data=request.data
            if((round(decimal.Decimal(data['monto_entregado']),2)>0)):
                id_user=data['funcionario_id']
                
                try:
                    codeUser=User.objects.get(id=id_user)
                except User.DoesNotExist:
                     return Response({'message':'No existe el usuario ingresado'},status=status.HTTP_406_NOT_ACCEPTABLE)      

                try:
                    dataCaja=Caja.objects.get(codigo_usuario=codeUser.pk)
                    dato=dataCaja.pk
                    data['caja_id']=dato
                except Caja.DoesNotExist:
                     return Response({'message':'No existe el registro de cajas para este usuario'},status=status.HTTP_406_NOT_ACCEPTABLE)      
                
                data['monto_entregado']
                data['monto_saldo']=data['monto_entregado']
                data=self.load_logs()
                data['fecha_entrega']=self.now_fecha()
                data['creado_en']=self.now_fecha()
                data['actualizado_en']=self.now_fecha()
                serializer = CuentasPorCobrarSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                cuenta_cobrar = serializer.create(serializer.validated_data)
                return Response({"message":"Se registro correctamente"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"Ingrese un valor numerico mayor a 0.0"},status=status.HTTP_406_NOT_ACCEPTABLE)
        except KeyError:
            return Response({'message':'Los campos usuario y monto entregado son requerido'},status=status.HTTP_406_NOT_ACCEPTABLE)      

        
    
class CuentaPorCobrarViewSet(ModelRetrieveUpdateListViewSet,LogMixin, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    model= CuentasPorCobrar
    serializer_class = CuentasPorCobrarSerializer
    lista_corte_moneda= CuentasPorCobrarListarSerializer
    
    def retrieve(self, request, *args, **kwargs):
        try:
            print("Detalles del id :============== ",kwargs["id"])
            cuenta_cobrar = CuentasPorCobrar.objects.get(id=kwargs["id"])
            if(cuenta_cobrar.eliminado_en is None):
                cuenta_serializer=self.lista_corte_moneda(cuenta_cobrar)
                return Response(cuenta_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Este registro esta eliminado"},status=status.HTTP_406_NOT_ACCEPTABLE)
        except CuentasPorCobrar.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_406_NOT_ACCEPTABLE)      

    def delete(self, request, *args, **kwargs):
        try:
            print("eliminando un  CuentasPorCobrar")
            eliminarCuenta = CuentasPorCobrar.objects.get(id=kwargs["id"])
            eliminarCuenta.eliminado_en=self.now_fecha()
            eliminarCuenta.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_202_ACCEPTED)
        except CuentasPorCobrar.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_406_NOT_ACCEPTABLE)

    def cobros(self, request, *args, **kwargs):
        try: 
            cuenta_cobrar = CuentasPorCobrar.objects.get(id=kwargs["id"])
            m_devuelto=0
            data=self.request.data
            m_devuelto=data['monto_devuelto_add']
            if(cuenta_cobrar.eliminado_en is None):
                if(round(decimal.Decimal(m_devuelto),2)>0):
                    cuenta_cobrar.monto_devuelto=cuenta_cobrar.monto_devuelto+round(decimal.Decimal(m_devuelto),2)
                    cuenta_cobrar.monto_saldo=cuenta_cobrar.monto_saldo-round(decimal.Decimal(m_devuelto),2)
                    m_devuelto=0
                    if(cuenta_cobrar.monto_entregado>=cuenta_cobrar.monto_devuelto):
                        data=self.load_logs() 
                        cuenta_cobrar.fecha_ultimo_pago=self.now_fecha()
                        cuenta_cobrar.actualizado_en=self.now_fecha()
                        if(cuenta_cobrar.monto_entregado==cuenta_cobrar.monto_devuelto):
                            cuenta_cobrar.estado="C"
                        serializer = CuentasPorCobrarSerializer(cuenta_cobrar,data=request.data, partial=True)
                        serializer.is_valid(raise_exception=True)
                        _cuentas=serializer.save()
                        return Response(CuentasPorCobrarSerializer(_cuentas).data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"message":"El monto ingresado es incorecto"},status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                        return Response({"message":"Ingrese el monto mayor a 0"},status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"message":"No se puede editar este registro esta eliminado"},status=status.HTTP_406_NOT_ACCEPTABLE)
            
        except KeyError:
            return Response({'message':'Ingrrese el monto en el campo monto_devuelto_add'},status=status.HTTP_406_NOT_ACCEPTABLE)      

#==================================transaccion inventarios jasper==========================
class InventarioViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    serializer_class = TransaccionInventarioSerializer
    
    def list(self, request, *args, **kwargs):
        return super(InventarioViewSet, self).list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = TransaccionInventario.objects.filter(eliminado_en=None)   
        return queryset
#==================================transaccion inventarios==========================
class TransaccionInventariosViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    #permission_classes = [IsAuthenticated]
    serializer_class_api = TransaccionInventarioSerializer
    lista_trasaccion_inventarios= TransaccionInventarioListarSerializer
    queryset=TransaccionInventario.objects.all()
    
    def list_api(self, request, *args, **kwargs):
        transaccion_inventario = TransaccionInventario.objects.filter(eliminado_en=None).order_by('-id')
        return Response(self.serializer_class_api(transaccion_inventario, many=True).data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        transaccion_inventario = TransaccionInventario.objects.filter(eliminado_en=None)
        return Response(self.lista_trasaccion_inventarios(transaccion_inventario, many=True).data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = TransaccionInventario.objects.filter(eliminado_en=None)   
        return queryset
    
    def create(self, request, *args, **kwargs):
        #data._mutable=True
        data=request.data
        data['caja_id']=self.caja()
        data=self.load_logs()
        data['fecha_transaccion']=self.now_fecha()
        data['creado_en']=self.now_fecha()
        serializer = TransaccionInventarioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        transaccion_inventario = serializer.create(serializer.validated_data)
        #return Response(self.get_serializer(transaccion_inventario).data, status=status.HTTP_201_CREATED)
        return Response({'messaje':'Se registro corectamente'},status=status.HTTP_201_CREATED)
        
class TransaccionInventarioViewSet(ModelRetrieveUpdateListViewSet,LogMixin, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    model= TransaccionInventario
    serializer_class = TransaccionInventarioSerializer
    lista_trasaccion_inventarios= TransaccionInventarioListarSerializer
    
    def retrieve(self, request, *args, **kwargs):
        try:
            print("Detalles del id :============== ",kwargs["id"])
            transaccion_inventario = TransaccionInventario.objects.get(id=kwargs["id"])
            if(transaccion_inventario.eliminado_en is None):
                cuenta_serializer=self.lista_trasaccion_inventarios(transaccion_inventario)
                return Response(cuenta_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Este registro esta eliminado"})
        except TransaccionInventario.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_406_NOT_ACCEPTABLE)      

    def delete(self, request, *args, **kwargs):
        try:
            print("eliminando un  TransaccionInventario")
            eliminar_tranzaccion = TransaccionInventario.objects.get(id=kwargs["id"])
            eliminar_tranzaccion.eliminado_en=self.now_fecha()
            eliminar_tranzaccion.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_202_ACCEPTED)
        except TransaccionInventario.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        try: 
            transaccion_inventario = TransaccionInventario.objects.get(id=kwargs["id"])
            if(transaccion_inventario.eliminado_en is None):
                data=self.request.data
                data=self.load_logs() 
                transaccion_inventario.actualizado_en=self.now_fecha()
                serializer = TransaccionInventarioSerializer(transaccion_inventario,data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                _transaccion=serializer.save()
                return Response(TransaccionInventarioSerializer(_transaccion).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"No se puede editar este registro esta eliminado"})
            
        except TransaccionInventario.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_406_NOT_ACCEPTABLE)
#######==================================================
#=================filtro de caja y arqueo
class FilterArqueoCaja(generics.ListAPIView):
    queryset = Caja.objects.all()
    serializer_class = ArqueoCajaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigo_caja_encabezadoarqueo']
#=======================================
class ArqueoCajaView(ArqueoViewSet, ModelRetrieveUpdateListViewSet,ActualizadoEncabezado,ActualizadoInventario):
    arqueo_detail=ArqueoCajaSerializer
    fecha=ActualizadoEncabezado
    def get_queryset(self):
        return Caja.objects.all()
 
    def retrieve(self, request, *args, **kwargs):

        fecha_busqueda=kwargs["fecha"]
        dt_obj = datetime.strptime(fecha_busqueda, '%d-%m-%y' ).date()
        envioarqueo=self.retrievefecha(dt_obj)
        envioinventario=self.inventaiofecha(dt_obj)
        arqueo_detalle = Caja.objects.get(id=kwargs["pk"])
        detalle_serializer=self.arqueo_detail(arqueo_detalle)
        return Response(detalle_serializer.data, status=status.HTTP_200_OK)
    
    
#======================usuaio filter=======================
class FilterUsuario(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name','last_name']


#==================================transaccion inventarios jasper==========================
class get_jasper(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    
    def list(self, request, *args, **kwargs):
        return super(InventarioViewSet, self).list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = TransaccionInventario.objects.filter(eliminado_en=None)   
        return queryset

