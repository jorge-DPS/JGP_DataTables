from re import S
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
from datetime import date, time, datetime

TIPO_HABILITADA= (
    ("V", _("Verdadero")),
    ("F", _("Falso")),
)
ESTADO_CAJA= (
    ("V", _("Vigente")),
    ("B", _("Bloqueado")),
)
class Caja(models.Model):
    descripcion_caja = models.CharField(
        verbose_name=_("Descripcion"),
        max_length=100,
        null=False, blank=False,
    ) 
    codigo_oficina = models.ForeignKey(
        'empresa.Sucursal',
        verbose_name="Codigo Oficina",
        related_name="codigo_oficina_caja",
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    saldo_minimo_mn = models.DecimalField(
        verbose_name=_("Saldo Minimo MN"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_maximo_mn = models.DecimalField(
        verbose_name=_("Saldo Maximo MN"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_minimo_me = models.DecimalField(
        verbose_name=_("Saldo Minimo ME"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_maximo_me = models.DecimalField(
        verbose_name=_("Saldo Maximo ME"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_minimo_mr = models.DecimalField(
        verbose_name=_("Saldo Minimo MR"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_maximo_mr = models.DecimalField(
        verbose_name=_("Saldo Maximo MR"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    codigo_usuario = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Codigo_Usuario"),
        related_name="codigo_usuario_caja",
        null=False, blank=False,
    )
    ultima_apertura = models.DateTimeField(
        verbose_name=_("Ultima Apertura"),
        null=True, blank=True,
    )
    ultimo_cuadre = models.DecimalField(
        verbose_name=_("Ultimo Cuadre"),
        max_digits=14, decimal_places=0,
        null=False, blank=False,
    )
    habilitada = models.CharField(
        max_length=1,
        verbose_name=_("Habilitada"),
        default="V",
        choices=TIPO_HABILITADA,
        null=False,blank=False,
    )
    saldo_mn = models.DecimalField(
        verbose_name=_("Saldo MN"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_me = models.DecimalField(
        verbose_name=_("Saldo ME"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    saldo_mr = models.DecimalField(
        verbose_name=_("Saldo MR"),
        max_digits=12, decimal_places=2,
        default=0.0,
        null=False, blank=False,
    )
    estado_caja = models.CharField(
        max_length=1,
        verbose_name=_("Estado Caja"),
        default="V",
        choices=ESTADO_CAJA,
        null=False,blank=False,
    )
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario actualizacion"),
        related_name="usuario_actualizacion_caja",
        null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal Creacion"),
        related_name="sucursal_creacion_caja",
        null=False, blank=False,
    )
    #campos log
    creado_en = models.DateTimeField(
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

    def __str__(self):
        return "%s" % (self.id)
    
    class Meta:
        db_table = "caj_cajas"
        verbose_name = _("Caja")
        verbose_name_plural = _("Cajas")
        unique_together = ('descripcion_caja',)

        