from os import stat
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from apps.accounts.api.v1 import serializers
from apps.contrib.api.viewsets import ModelCreateListViewSet, ModelUpdateListViewSet, ModelRetrieveUpdateListViewSet
from apps.contrib.api.exceptions import NotFound
from apps.credito.models import (EvaluacionEconomica,
                                Venta,Compra,
                                GastoOperativoMes,
                                GastoFamiliarMes,
                                ObligacionMes,
                                OtroIngreso,
                                Pendiente)

from apps.contrib.api.viewsets import ModelCreateListViewSet
from apps.contrib.api.viewsets import PermissionViewSet
from apps.contrib.api.viewsets import (ModelCreateListViewSet, 
                                        ModelRetrieveUpdateListViewSet, PermissionlMixin)
from datetime import datetime
from apps.credito.api.v1.serializers.credito import (
                                                    PendienteSerializer,
                                                    OtroIngresoSerializer,
                                                    ObligacionMesSerializer,
                                                    GastoFamiliarMesSerializer,
                                                    GastoOperativoMesMesSerializer,
                                                    VentaSerializer,
                                                    CompraSerializer,
                                                    EvaluacionEconomicaSerializer,
                                                    EvaluacionEconomicaRetrieveSerializer
    
                                                  )

class LogMixin(object):
    def load_logs(self):
        data=self.request.data
        data['usuario_actualizacion']=self.request.user.pk
        data['sucursal_creacion']=self.request.user.branch_office.pk
        return data
    def now_fecha(self):
        tiempo = datetime.now()
        fechahora = tiempo.replace(microsecond=0)
        data=fechahora
        return data
#==================================Evaluacion Economica==========================   
class EvaluacionesEconimincaViewSet(PermissionViewSet, ModelCreateListViewSet,LogMixin):
    serializer_class = EvaluacionEconomicaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = EvaluacionEconomica.objects.filter(eliminado_en=None)
        return queryset
    
    def list(self, request, *args, **kwargs):
        evaluacion = EvaluacionEconomica.objects.filter(eliminado_en=None).order_by('-id')
        return Response(self.get_serializer(evaluacion, many=True).data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        data=request.data
        print("========datos de post===",data)
        data=self.load_logs()
        data['creado_en']=self.now_fecha()
        evaluacion_serializer=EvaluacionEconomicaSerializer(data=data)
        evaluacion_serializer.is_valid(raise_exception=True)
        evaluacion=evaluacion_serializer.create(evaluacion_serializer._validated_data)
        
        #================Venta===========================
        data_venta=data['venta_evaluacion_economica']
        #del data['venta_evaluacion_economica']
        #================Compra===========================
        data_compra=data['compra_evaluacion_economica']
        #del data['compra_evaluacion_economica']
        #================gasto operativo===========================
        data_gasto_operativo=data['gasto_operativo_evaluacion_economica']
        del data['gasto_operativo_evaluacion_economica']
        #================gasto familiar===========================
        data_gasto_familiar=data['gasto_familiar_evaluacion_economica']
        del data['gasto_familiar_evaluacion_economica']
        #================Obligacion===========================
        data_obligacion=data['obligacion_evaluacion_economica']
        del data['obligacion_evaluacion_economica']
        #================Otro ingreso===========================
        data_otro_ingreso=data['otro_ingreso_evaluacion_economica']
        del data['otro_ingreso_evaluacion_economica']
        #================Otro ingreso===========================
        data_pendiente=data['pendiente_evaluacion_economica']
        del data['pendiente_evaluacion_economica']
        
        #if request.data["compra_evaluacion_economica"] :
        for detalle in data_venta:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_venta(detalle)
            
        for det_compra in data_compra:
            print("**************************entrando compra")
            
            det_compra['evaluacion_id']=evaluacion.id
            det_compra['usuario_actualizacion']=self.request.user.pk
            det_compra['sucursal_creacion']=self.request.user.branch_office.pk
            det_compra['creado_en']=self.now_fecha()
            self.create_compra(det_compra)
            print("*******************saleeeeeeeeeeeeeeeee")
            
        
        for detalle in data_gasto_operativo:
            print("**************************entrando operativo")
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_operativo(detalle)
            print("*******************saleeeeeeeeeeeeeeeee")
            
        for detalle in data_gasto_familiar:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_familiar(detalle)
        
        for detalle in data_obligacion:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_obligacion(detalle)
        
        for detalle in data_otro_ingreso:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_otro_ingreso(detalle)
        
        for detalle in data_pendiente:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_pendiente(detalle)
        
        data_nuevo={"message":"Se registro corectamente"}
        return Response(data_nuevo,status=status.HTTP_204_NO_CONTENT)
   
    def create_venta(self,data):
        serializer=VentaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion

    def create_compra(self,data):
        serializer=CompraSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        compra_evaluacion=serializer.create(serializer.validated_data)
        return compra_evaluacion
    
    def create_operativo(self,data):
        serializer=GastoOperativoMesMesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_familiar(self,data):
        serializer=GastoFamiliarMesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_obligacion(self,data):
        serializer=ObligacionMesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_otro_ingreso(self,data):
        serializer=OtroIngresoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_pendiente(self,data):
        serializer=PendienteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
#====================================UPDATE DELETE RETRIEVE=================================    
class EvaluacionEconimincaViewSet(IsAuthenticated, ModelRetrieveUpdateListViewSet,LogMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = EvaluacionEconomicaSerializer
    serializer_class_retrieve = EvaluacionEconomicaRetrieveSerializer

    def get_queryset(self):
        return EvaluacionEconomica.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        
        evaluacion = EvaluacionEconomica.objects.get(id=kwargs["pk"])
        
        if(evaluacion.eliminado_en is None):
           
            evaluacion_serializer=self.serializer_class_retrieve(evaluacion)
            return Response(evaluacion_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"Este registro esta eliminado"})
    
    def update(self, request, *args, **kwargs):
        evaluacion=EvaluacionEconomica.objects.get(id=kwargs["pk"])
        data=self.request.data
        evaluacion.actualizado_en=self.now_fecha()
        serializer = EvaluacionEconomicaSerializer(evaluacion,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #=====================elimina las anteriores=============
        venta=Venta.objects.filter(evaluacion_id=kwargs["pk"])
        compra=Compra.objects.filter(evaluacion_id=kwargs["pk"])
        operativo=GastoOperativoMes.objects.filter(evaluacion_id=kwargs["pk"])
        familiar=GastoFamiliarMes.objects.filter(evaluacion_id=kwargs["pk"])
        obligacion=ObligacionMes.objects.filter(evaluacion_id=kwargs["pk"])
        ingreso=OtroIngreso.objects.filter(evaluacion_id=kwargs["pk"])
        pendiente=Pendiente.objects.filter(evaluacion_id=kwargs["pk"])
        for datos in venta:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save()
        for datos in compra:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save()
        for datos in operativo:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save()
        for datos in familiar:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save()
        for datos in obligacion:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save()
        for datos in ingreso:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save()
        for datos in pendiente:
            datos.actualizado_en=self.now_fecha()
            datos.eliminado_en=self.now_fecha()
            datos.save() 
        #========================================================
        print("================almacenado final",serializer)
        data=request.data
       #================Venta===========================
        data_venta=data['venta_evaluacion_economica']
        del data['venta_evaluacion_economica']
        #================Compra===========================
        data_compra=data['compra_evaluacion_economica']
        del data['compra_evaluacion_economica']
        #================gasto operativo===========================
        data_gasto_operativo=data['gasto_operativo_evaluacion_economica']
        del data['gasto_operativo_evaluacion_economica']
        #================gasto familiar===========================
        data_gasto_familiar=data['gasto_familiar_evaluacion_economica']
        del data['gasto_familiar_evaluacion_economica']
        #================Obligacion===========================
        data_obligacion=data['obligacion_evaluacion_economica']
        del data['obligacion_evaluacion_economica']
        #================Otro ingreso===========================
        data_otro_ingreso=data['otro_ingreso_evaluacion_economica']
        del data['otro_ingreso_evaluacion_economica']
        #================PENDIENTE===========================
        data_pendiente=data['pendiente_evaluacion_economica']
        del data['pendiente_evaluacion_economica']
        
        #if request.data["compra_evaluacion_economica"] :
        for detalle in data_venta:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_venta(detalle)
            
        for det_compra in data_compra:
            print("**************************entrando compra")
            
            det_compra['evaluacion_id']=evaluacion.id
            det_compra['usuario_actualizacion']=self.request.user.pk
            det_compra['sucursal_creacion']=self.request.user.branch_office.pk
            det_compra['creado_en']=self.now_fecha()
            self.create_compra(det_compra)
            print("*******************saleeeeeeeeeeeeeeeee")
            
        for detalle in data_gasto_operativo:
            print("**************************entrando operativo")
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_operativo(detalle)
            print("*******************saleeeeeeeeeeeeeeeee")
            
        for detalle in data_gasto_familiar:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_familiar(detalle)
        
        for detalle in data_obligacion:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_obligacion(detalle)
        
        for detalle in data_otro_ingreso:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_otro_ingreso(detalle)
        
        for detalle in data_pendiente:
            detalle['evaluacion_id']=evaluacion.id
            detalle['usuario_actualizacion']=self.request.user.pk
            detalle['sucursal_creacion']=self.request.user.branch_office.pk
            detalle['creado_en']=self.now_fecha()
            self.create_pendiente(detalle)
        
        data_nuevo={"message":"Se edito corectamente"}
        return Response(data_nuevo,status=status.HTTP_204_NO_CONTENT)
        
    def create_venta(self,data):
        serializer=VentaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion

    def create_compra(self,data):
        serializer=CompraSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        compra_evaluacion=serializer.create(serializer.validated_data)
        return compra_evaluacion
    
    def create_operativo(self,data):
        serializer=GastoOperativoMesMesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_familiar(self,data):
        serializer=GastoFamiliarMesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_obligacion(self,data):
        serializer=ObligacionMesSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_otro_ingreso(self,data):
        serializer=OtroIngresoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
    
    def create_pendiente(self,data):
        serializer=PendienteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        evaluacion=serializer.create(serializer.validated_data)
        return evaluacion
        
    
    def delete (self, request, *args, **kwargs):
        try:
            print("******************** Eliminando evaluacion: ", kwargs["pk"])
            evaluacion = EvaluacionEconomica.objects.get(pk=kwargs["pk"])
            evaluacion.eliminado_en=self.now_fecha()
            evaluacion.save()
            venta=Venta.objects.filter(evaluacion_id=kwargs["pk"])
            compra=Compra.objects.filter(evaluacion_id=kwargs["pk"])
            operativo=GastoOperativoMes.objects.filter(evaluacion_id=kwargs["pk"])
            familiar=GastoFamiliarMes.objects.filter(evaluacion_id=kwargs["pk"])
            obligacion=ObligacionMes.objects.filter(evaluacion_id=kwargs["pk"])
            ingreso=OtroIngreso.objects.filter(evaluacion_id=kwargs["pk"])
            pendiente=Pendiente.objects.filter(evaluacion_id=kwargs["pk"])
            for datos in venta:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            for datos in compra:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            for datos in operativo:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            for datos in familiar:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            for datos in obligacion:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            for datos in ingreso:
                datos.eliminado_en=self.now_fecha()
                datos.save()
            for datos in pendiente:
                datos.eliminado_en=self.now_fecha()
                datos.save()        
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
    
    
    