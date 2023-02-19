from random import choices
from tabnanny import verbose
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from datetime import datetime
from django.utils import timezone
from apps.accounts.models.user import User
from apps.empresa.models.sucursal import Sucursal
from apps.administracion.models.persona import Persona
import json
from rest_framework.parsers import JSONParser

CICLO_ROTACION= (
    ("D", _("Diario")),
    ("S", _("Semanal")),
    ("Q", _("Quincenal")),
    ("M", _("Mensual")),
)

ACTIVIDAD_EVALUADA= (
    ("C", _("Comercio")),
    ("P", _("Produccion")),
    ("S", _("Servicio")),
)
GENERO= (
    ("M", _("Masculino")),
    ("F", _("Femenino")),
)

NIVEL_ESTUDIO= (
    ("K", _("Kinder")),
    ("P", _("Primaria")),
    ("S", _("Secundaria")),
    ("T", _("Tecnica")),
    ("U", _("Universitaria")),
    ("N", _("Sin Formacion")),
)

class EvaluacionEconomica(models.Model):

    persona_id = models.ForeignKey(
        'administracion.Persona',
        verbose_name="Persona",
        related_name="persona_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )

    actividad_evaluada = models.CharField(
        verbose_name=_('Actividad evaluada'),
        max_length=1,
        choices=ACTIVIDAD_EVALUADA,
        blank = False, null = False 
    )
    
    actividad_principal = models.CharField(
        verbose_name=_('Actividad Principal'),
        max_length=100,
        blank = False, null = False 
    )
    
    ciclo_rotacion = models.CharField(
        verbose_name=_('Ciclo rotacion'),
        max_length=1,
        choices=CICLO_ROTACION,
        blank = False, null = False 
    )
    
    compra_aproximada_mensuales = models.DecimalField(
        verbose_name=_("Compra aproximada mensualidad"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    ventas_aproximada_lunes = models.DecimalField(
        verbose_name=_("Ventas aproximada Lunes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    ventas_aproximada_martes = models.DecimalField(
        verbose_name=_("Ventas aproximada martes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    ventas_aproximada_miercoles = models.DecimalField(
        verbose_name=_("Ventas aproximada miercoloes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )

    ventas_aproximada_jueves = models.DecimalField(
        verbose_name=_("Ventas aproximada jueves"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    ventas_aproximada_viernes = models.DecimalField(
        verbose_name=_("Ventas aproximada viernes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    ventas_aproximada_sabado = models.DecimalField(
        verbose_name=_("Ventas aproximada sabado"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    ventas_aproximada_domingo = models.DecimalField(
        verbose_name=_("Ventas aproximada domingo"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    ventas_aproximada_mensuales = models.DecimalField(
        verbose_name=_("Ventas aproximada mensuales"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    numero_dependiente = models.SmallIntegerField(
        verbose_name=_('numero_dependiente'),
        blank = False, null = False,
        default = 0
    )
    
    venta_elegida = models.DecimalField(
        verbose_name=_("Ventas elegidas"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    compras = models.DecimalField(
        verbose_name=_("Compras"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    utilidad_bruta = models.DecimalField(
        verbose_name=_("Utilidad bruta"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    margen_utilidad_bruta = models.DecimalField(
        verbose_name=_("Margen utilidad bruta"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )

    def save(self, *args, **kwargs):
        self.actividad_principal = " ".join((self.actividad_principal).lower().capitalize().split())
        return super(EvaluacionEconomica, self).save(*args, **kwargs)
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'evaluacion_economica_comercio_produccion'
        verbose_name = "Evaluacion Economica"
        verbose_name_plural = "Evaluaciones Economicas"
        
class Venta(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="venta_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    
    producto_servicio = models.CharField(
        verbose_name=_('Producto servicio'),
        max_length=30,
        blank = False, null = False 
    )     
    
    unidad_venta = models.IntegerField(
        verbose_name=_("Unidad de venta"),
        null=False, blank=False,
    )
    
    cantidad_venta = models.IntegerField(
        verbose_name=_("Cantidad de venta"),
        null=False, blank=False,
    )
    
    precio_venta = models.DecimalField(
        verbose_name=_("Precio de venta"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    frecuencia_venta = models.IntegerField(
        verbose_name=_("Frecuencia de venta"),
        null=False, blank=False,
    )
    
    ventas_mes = models.DecimalField(
        verbose_name=_("ventas del mes"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def save(self, *args, **kwargs):
        self.producto_servicio = " ".join((self.producto_servicio).lower().capitalize().split())
        return super(Venta, self).save(*args, **kwargs)
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'venta'
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
class Compra(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="compra_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    
    producto_insumo = models.CharField(
        verbose_name=_('Producto insumo'),
        max_length=30,
        blank = False, null = False 
    )     
    
    unidad_compra = models.IntegerField(
        verbose_name=_("Unidad de compra"),
        null=False, blank=False,
    )
    
    cantidad_compra = models.IntegerField(
        verbose_name=_("Cantidad de compra"),
        null=False, blank=False,
    )
    
    precio_compra = models.DecimalField(
        verbose_name=_("Precio de compra"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    frecuencia_compra = models.IntegerField(
        verbose_name=_("Frecuencia de compra"),
        null=False, blank=False,
    )
    
    compras_mes = models.DecimalField(
        verbose_name=_("Compras del mes"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def save(self, *args, **kwargs):
        self.producto_insumo = " ".join((self.producto_insumo).lower().capitalize().split())
        return super(Compra, self).save(*args, **kwargs)
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'compra'
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        
class GastoOperativoMes(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="gasto_operativo_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    
    alquileres = models.DecimalField(
        verbose_name =_("Alquileres del mes"),
        max_digits = 12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )     
    
    agua = models.DecimalField(
        verbose_name=_("Agua del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    electricidad = models.DecimalField(
        verbose_name =_("Electricidad del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    telefono = models.DecimalField(
        verbose_name =_("Telefono del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    impuesto = models.DecimalField(
        verbose_name =_("Impuesto del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    transporte = models.DecimalField(
        verbose_name =_("Transporte del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    salarios = models.DecimalField(
        verbose_name =_("Salarios del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    mantenimiento = models.DecimalField(
        verbose_name =_("Mantenimiento del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
            
    reparaciones = models.DecimalField(
        verbose_name =_("Reparaciones del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    otros = models.DecimalField(
        verbose_name =_("Otros del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'gasto_operativo_mes'
        verbose_name = "Gasto Operativo"
        verbose_name_plural = "Gastos Operativos"
        
class GastoFamiliarMes(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="gasto_familiar_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    
    alimentacion = models.DecimalField(
        verbose_name =_("Alimentacion del mes"),
        max_digits = 12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )     
    
    vivienda = models.DecimalField(
        verbose_name =_("Vivienda del mes"),
        max_digits = 12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    electricidad = models.DecimalField(
        verbose_name =_("Electricidad del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    agua = models.DecimalField(
        verbose_name=_("Agua del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    educacion = models.DecimalField(
        verbose_name =_("Educacion del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    transporte = models.DecimalField(
        verbose_name =_("Transporte del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    salud = models.DecimalField(
        verbose_name =_("Salud del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )   
    
    vestuario = models.DecimalField(
        verbose_name =_("Vestuario del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    telefono = models.DecimalField(
        verbose_name =_("Telefono del mes"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
         
    recreacion = models.DecimalField(
        verbose_name =_("Recreacion del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    otros = models.DecimalField(
        verbose_name =_("Otros del mes"),
        max_digits = 12, decimal_places = 2,
        default=0.0,
        null=False, blank = False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'gasto_familiar_mes'
        verbose_name = "Gasto Familiar"
        verbose_name_plural = "Gastos Familiares"
        
class ObligacionMes(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="obligacion_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    
    detalle = models.CharField(
        verbose_name=_('Detalle del mes'),
        max_length=30,
        blank = False, null = False 
    )      
    
    saldo_deudor = models.DecimalField(
        verbose_name =_("Saldo deudor del mes"),
        max_digits = 12, decimal_places=2,
        null=False, blank=False,
    )
    
    cuota_mes = models.DecimalField(
        verbose_name =_("Cuota mes del mes"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def save(self, *args, **kwargs):
        self.detalle = " ".join((self.detalle).lower().capitalize().split())
        return super(ObligacionMes, self).save(*args, **kwargs)
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'obligacion_mes'
        verbose_name = "Obligacion de Mes"
        verbose_name_plural = "Obligaciones del Mes"

class OtroIngreso(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="otro_ingreso_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )    
    
    conyugue = models.DecimalField(
        verbose_name =_("Conyugue"),
        max_digits = 12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    otro_negocio = models.DecimalField(
        verbose_name =_("Otro negocio"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    rentas = models.DecimalField(
        verbose_name =_("Rentas"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    otro_ingresos = models.DecimalField(
        verbose_name =_("Otro ingresos"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'otro_ingreso'
        verbose_name = "Otro Ingreso"
        verbose_name_plural = "Otros Ingresos"

class Pendiente(models.Model):
    
    evaluacion_id = models.ForeignKey(
        'EvaluacionEconomica',
        verbose_name="Codigo de Evaluacion economica",
        related_name="pendiente_evaluacion_economica",
        on_delete=models.CASCADE,
        null=False, blank=False
    )    
    
    edad = models.PositiveSmallIntegerField(
        verbose_name=_('Edad'),
        blank = False, null = False,
    )
    
    genero = models.CharField(
        verbose_name=_('Genero'),
        max_length=1,
        choices=GENERO,
        blank = False, null = False 
    )
    
    nivel_estudio = models.CharField(
        verbose_name=_('Nivel de estudio'),
        max_length=1,
        choices=NIVEL_ESTUDIO,
        blank = False, null = False 
    )
    
    usuario_actualizacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    sucursal_creacion = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    def str(self):
        return "%s " % (self.id)
    
    class Meta:
        app_label = 'credito'
        db_table = 'dependiente'
        verbose_name = "Dependiente"
        verbose_name_plural = "Dependientes"
       

   
 
    
    
    
    
    
    




    
    
    

    