from django.db import models
from django.db.models import Q
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from apps.contrib.utils.strings import get_uuid
from apps.accounts.models.user import User
from django.core.validators import MaxValueValidator, MinValueValidator

TIPO_MOVIMIENTO = (
    ("E", _("Entrada")),
    ("S", _("Salida")),
)
ESTADO_CUENTAS = (
    ("P", _("Pendiente")),
    ("C", _("Cancelado")),
)
class Caja(models.Model):
    codigo_caja = models.IntegerField(
        verbose_name=_("Codigo Caja"),
        help_text=_("Codigo de Caja"),
        null=True, blank=True,
    )
    descripcion = models.CharField(
        verbose_name=_("Descripcion"),
        max_length=150,
        null=True, blank=True,
    ) 
    sucursal = models.ForeignKey(
        'empresa.Sucursal',
        verbose_name="Sucursal",
        related_name="caja_sucursal",
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return "%s" % (self.codigo_caja)

    class Meta:
        db_table = "caja"
        verbose_name = _("Caja")
        verbose_name_plural = _("Cajas")

class EncabezadoArqueo(models.Model):
    cajero = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Cajero"),
        related_name="encabezado_user",
        null=True, blank=True,
    )
    caja = models.ForeignKey(
        'Caja',
        verbose_name=_("Caja"),
        related_name="encabezado_caja",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    fecha = models.DateField(
        verbose_name=_("Fecha"),
        null=True, blank=True,
    )
    total_sistema_a = models.DecimalField(
        verbose_name=_("Total A"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    total_sistema_b = models.DecimalField(
        verbose_name=_("Total B"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    total_material_monetario_mn = models.DecimalField(
        verbose_name=_("Total Moneda Nacional"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    total_material_monetario_me = models.DecimalField(
        verbose_name=_("Total Moneda Extranjera"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )

    def __str__(self):
        return "%s" % (self.id)
    
    class Meta:
        db_table = "encabezado_arqueo"
        verbose_name = _("Encabezado")
        verbose_name_plural = _("Encabezados")


class DetalleArqueo(models.Model):
    encabezado = models.ForeignKey(
        'EncabezadoArqueo',
        verbose_name=_("Encabezado"),
        related_name="detalle_arqueo_encabezado",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    tipo_moneda = models.IntegerField(
        verbose_name=_("Tipo moneda"),
        help_text=_("Este es el tipo de moneda"),
        default = 0,
        null=True, blank=True,
    )
    corte = models.DecimalField(
        verbose_name=_("Corte de moneda"),
        max_digits=8, decimal_places=2,
        null=True, blank=True,
    )
    cantidad = models.IntegerField(
        verbose_name=_("Cantidad"),
        help_text=_("Cantidad"),
        default = 0,
        null=True, blank=True,
    )
    total = models.DecimalField(
        verbose_name=_("Total Efectivo"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    
    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        db_table = "detalle_arqueo"
        verbose_name = _("Detalle Arqueo")
        verbose_name_plural = _("Detalles Arqueos")

class MovimientoDia(models.Model):
    encabezado = models.ForeignKey(
        'EncabezadoArqueo',
        verbose_name=_("Encabezado"),
        related_name="movimiento_dia_encabezado",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    caja = models.ForeignKey(
        'Caja',
        verbose_name=_("Caja"),
        related_name="movimiento_dia_caja",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    codigo_producto_financiero = models.IntegerField(
        verbose_name=_("Codigo Producto"),
        help_text=_("Este es el codigo que se usa para productos"),
        default = 0,
        null=True, blank=True,
    )
    detalle = models.TextField(
        verbose_name=_("Detalle"),
        null=True, blank=True,
    )
    tipo_movimiento = models.CharField(
        max_length=1,
        verbose_name=_("Tipo Movimiento"),
        choices=TIPO_MOVIMIENTO,
        blank=True,
        null=True,
    )
    monto_a = models.DecimalField(
        verbose_name=_("Monto A"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    monto_b = models.DecimalField(
        verbose_name=_("Monto B"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    fecha_proceso_movimiento = models.DateField(
        verbose_name=_("Fecha Proceso"),
        null=True, blank=True,
    )
    
    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        db_table = "movimiento_dia"
        verbose_name = _("Movimiento Dia")
        verbose_name_plural = _("Movimientos Dias")

class SaldoProducto(models.Model):
    caja = models.ForeignKey(
        'Caja',
        verbose_name=_("Caja"),
        related_name="saldo_producto_caja",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    codigo_producto_financiero_saldo = models.IntegerField(
        verbose_name=_("Codigo Producto"),
        help_text=_("Este es el codigo que se usa para productos"),
        default = 0,
        null=True, blank=True,
    )
    saldo_sistema_a = models.DecimalField(
        verbose_name=_("Saldo A"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    saldo_sistema_b = models.DecimalField(
        verbose_name=_("Saldo B"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    fecha_proceso = models.DateField(
        verbose_name=_("Fecha Proceso"),
        null=True, blank=True,
    )

    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        db_table = "saldo_producto"
        verbose_name = _("Saldo Producto")
        verbose_name_plural = _("Saldos Productos")

class CuentasRendir(models.Model):
    caja = models.ForeignKey(
        'Caja',
        verbose_name=_("Caja"),
        related_name="cuenta_rendir_caja",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    fecha_transaccion = models.DateField(
        verbose_name=_("Fecha transaccion"),
        null=True, blank=True,
    )
    usuario = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario"),
        related_name="cuentas_rendir_usuario",
        null=True, blank=True,
    )
    monto_entregado = models.DecimalField(
        verbose_name=_("Monto Entregado"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    monto_recuperado = models.DecimalField(
        verbose_name=_("Monto Recuperado"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    saldo = models.DecimalField(
        verbose_name=_("Saldo"),
        max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    estado = models.CharField(
        max_length=1,
        verbose_name=_("Tipo Movimiento"),
        choices=ESTADO_CUENTAS,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        db_table = "cuentas_rendir"
        verbose_name = _("Cuenta Rendir")
        verbose_name_plural = _("Cuentas Rendir")
