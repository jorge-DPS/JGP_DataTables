
from re import S
from sre_parse import Verbose
from tabnanny import verbose
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from datetime import date
from datetime import datetime
from django.utils import timezone
from apps.accounts.models.user import User
from apps.empresa.models.sucursal import Sucursal
from apps.cajas.models.caja import Caja
import json
import jsonfield
from rest_framework.parsers import JSONParser

_PRODUCTO_FINANCIERO= (
    (51, _("Electrodomesticos")),
    (52, _("Viveres")),
    (53, _("Temporada")),
    (54, _("Articulos del Hogar")),
    (55, _("Otros")),
)
_ESTADOS= (
    ("P", _("Pendiente")),
    ("C", _("Cancelado")),
)
_ESTADOS_FONDO= (
    ("A", _("Fondo A")),
    ("B", _("Fondo B")),
)
class CuentasPorCobrar(models.Model):
    caja_id = models.ForeignKey(
        'cajas.Caja',
        verbose_name="Codigo Caja",
        related_name="codigo_caja_cuentasporcobrar",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    funcionario_id = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Codigo Funcionario"),
        related_name="codigo_funcionario_cuentasporcobrar",
        null=False, blank=False,
    )
    fecha_entrega = models.DateTimeField(
        verbose_name=_("Fecha Entrega"),
        null=False, blank=False,
    )
    monto_entregado = models.DecimalField(
        verbose_name=_("Monto por cobrar"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    monto_devuelto = models.DecimalField(
        verbose_name=_("Monto a Cuenta"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    monto_saldo = models.DecimalField(
        verbose_name=_("monto Saldo"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    fecha_ultimo_pago = models.DateTimeField(
        verbose_name=_("Ultima Fecha Pago"),
        null=True, blank=True,
    )
    estado = models.CharField(
        max_length=1,
        verbose_name=_("Estado"),
        choices=_ESTADOS,
        default="P",
        null=False,blank=False,
    )
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario actualizacion"),
        related_name="usuario_actualizacion_cuentasporcobrar",
        null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal Creacion"),
        related_name="sucursal_creacion_cuentasporcobrar",
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        verbose_name=("Fecha creacion"),
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
    def __str__(self):
        return "%s" % (self.id)
    
    class Meta:
        db_table = "caj_cuentas_por_cobrar"
        verbose_name = _("Cuenta por Cobrar")
        verbose_name_plural = _("Cuentas por Cobrar")

class TransaccionInventario(models.Model):
    caja_id = models.ForeignKey(
        'cajas.Caja',
        verbose_name="Codigo Caja",
        related_name="codigo_caja_transaccioninventario",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    fecha_transaccion = models.DateTimeField(
        verbose_name=("Fecha Transaccion"),
        null=False, blank=False
    )
    producto_financiero_id = models.PositiveSmallIntegerField(
        verbose_name=_("Codigo Producto Financiero"),
        choices=_PRODUCTO_FINANCIERO,
        null=False,blank=False,
    )
    detalle = models.TextField(
        verbose_name=_("Detalle"),
        null=False, blank=False,
    )
    fondo = models.CharField(
        max_length=1,
        verbose_name=_("Fondo"),
        choices=_ESTADOS_FONDO,
        null=False,blank=False,
    )
    monto_ingreso = models.DecimalField(
        verbose_name=_("Monto Ingreso"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    monto_salida = models.DecimalField(
        verbose_name=_("Monto Salida"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario actualizacion"),
        related_name="usuario_actualizacion_transaccioninventario",
        null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal Creacion"),
        related_name="sucursal_creacion_transaccioninventario",
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha Actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    def save(self, *args, **kwargs):
        self.detalle = " ".join((self.detalle).lower().capitalize().split())
        return super(TransaccionInventario, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.id)
    
    class Meta:
        db_table = "caj_transaccion_inventario"
        verbose_name = _("Transaccion Inventario")
        verbose_name_plural = _("Transacciones Inventarios")

class EncabezadoArqueo(models.Model):
    caja_id = models.ForeignKey(
        'cajas.Caja',
        verbose_name="Codigo Caja",
        related_name="codigo_caja_encabezadoarqueo",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    usuario_id = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Codigo Usiario"),
        related_name="codigo_usuario_encabezadoarqueo",
        null=False, blank=False,
    )
    fecha_arqueo = models.DateTimeField(
        verbose_name=("Fecha arqueo"),
        null=False, blank=False,
    )
    total_arqueo_mn = models.DecimalField(
        verbose_name=_("Total Arqueo MN"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    total_arqueo_me = models.DecimalField(
        verbose_name=_("Total Arqueo ME"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    observaciones = models.TextField(
        verbose_name=_("Observaciones"),
        null=True, blank=True,
    )
    arqueo_definitivo =models.BooleanField(
        default=True,
        verbose_name=_("¿Es arqueo definitivo?"),
        null=False, blank=False,
    )
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario actualizacion"),
        related_name="usuario_actualizacion_encabezado_arqueo",
        #null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal Creacion"),
        related_name="sucursal_creacion_encabezadoarqueo",
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha Actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    
    def __str__(self):
        return "%s" % (self.id)
    
    class Meta:
        db_table = "caj_arqueo"
        verbose_name = _("Encabezado Arqueo")
        verbose_name_plural = _("Encabezados Arqueos")

class DetalleArqueo(models.Model):
    arqueo_id = models.ForeignKey(
        'EncabezadoArqueo',
        verbose_name=_("Arqueo Id"),
        related_name="detalle_arqueo_encabezado",
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    corte_moneda_id = models.ForeignKey(
        'CorteMoneda',
        verbose_name=_("Corte Moneda"),
        related_name="corte_moneda",
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    
    moneda_id= models.PositiveSmallIntegerField(
        verbose_name=_("Moneda"),
        null=False,blank=False,
    )
    
    cantidad_corte_moneda = models.IntegerField(
        verbose_name=_("Cantidad Corte Moneda"),
        help_text=_("Cantidad corte moneda"),
        null=False, blank=False,
    )
    
    valor_corte_moneda = models.DecimalField(
        verbose_name=("Valor Corte moneda"),
        max_digits=12, decimal_places=2,
        null=False, blank=False,
    )
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario actualizacion"),
        related_name="usuario_actualizacion_detalle_arqueo",
        null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal Creacion"),
        related_name="sucursal_creacion_detalle_arqueo",
        null=False, blank=False,
    )
    #campos log
    
    creado_en = models.DateTimeField(
        #verbose_name = _("Fecha Creacion"),
        auto_now_add=True,
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    @property
    def detalles(self):
        detalles=DetalleArqueo.objects.filter(arqueo_id=self)
        return detalles

    class Meta:
        db_table = "caj_detalle_arqueo"
        verbose_name = _("Detalle Arqueo")
        verbose_name_plural = _("Detalles Arqueos")        

    def __str__(self):
        return "%s %s" % (
            self.cantidad_corte_moneda,
            self.valor_corte_moneda    
        )

class CorteMoneda(models.Model):
    moneda_id= models.PositiveSmallIntegerField(
        verbose_name=_("Moneda"),
        null=False,blank=False,
    )
    
    descripcion_corte_moneda = models.CharField(
        verbose_name=_("Descripcion corete moneda"),
        max_length=100,
        null=False, blank=False,
    )
    
    valor_corte_moneda = models.DecimalField(
        verbose_name=_("Valor Corte moneda"),
        max_digits=5, decimal_places=2,
        null=False, blank=False,
    )
    
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario actualizacion"),
        related_name="usuario_actualizacion_corte_moneda",
        null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal Creacion"),
        related_name="sucursal_creacion_corte_moneda",
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        verbose_name=("Fecha Actualizacion"),
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )

    
    class Meta:
        db_table = "caj_cortes_monedas"
        verbose_name = _("Corte Moneda")
        verbose_name_plural = _("Cortes Monedas")
    
    def __str__(self):
        return "%s" % (self.descripcion_corte_moneda)
    


