from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.contrib.utils.files import clean_static_url
from apps.contrib.utils.strings import get_uuid5

from apps.accounts.models.user import User
from apps.empresa.models.sucursal import Sucursal
from datetime import date, time, datetime

ESTADO_DEPOSITO= (
    ("P", _("Pendiente")),
    ("A", _("Aplicado")),
)

_NUMERO_CUENTA= (
    (1, _("BISA - 777342 401 7")),
    (2, _("BNB - 1502360716")),
    (3, _("Economico - 2051563479")),
    (4, _("Mercantil - 4068641015")),
    (5, _("Solidario - 311780 000 001")),
    (6, _("Solidario - 311780 000 002")),
    (7, _("Solidario - 311780 000 003")), 
    (8, _("Solidario - 311780-000-001")),
    (9, _("Solidario - 311780-000-002")), 
    (10, _("Solidario - 311780-000-003")),
    (11, _("Union - 10000030927541")),
)


class Deposito(models.Model):
    """Creacion extracto Deposito model."""
    numero_cuenta = models.PositiveSmallIntegerField(
        verbose_name=_('Numero cuenta'),
        choices=_NUMERO_CUENTA,
        blank = False, null = False,
    )
    fecha_deposito = models.CharField(
        max_length=19,
        null=False, blank=False,
    )
    descripcion = models.CharField(
        verbose_name=_('Descripcin de extracto deposito'),
        max_length=250,
        blank = False, null = False 
    )
    numero_transaccion = models.CharField(
        verbose_name=_('Numero transaccion'),
        max_length=250,
        unique = True,
        blank = False, null = False 
    )
    monto_mn = models.DecimalField(
        verbose_name=_("Monto mn"),
        max_digits=8, decimal_places=2,
        null=False, blank=False,
    )
    
    estado = models.CharField(
        max_length=1,
        verbose_name=_("Estado"),
        default="P",
        choices=ESTADO_DEPOSITO,
        null=False,blank=False,
    )
    #campos log
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
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
   
    def save(self, *args, **kwargs):
        self.descripcion = " ".join((self.descripcion).lower().capitalize().split())
        return super(Deposito, self).save(*args, **kwargs)
    
    def str(self):
        return self.numero_cuenta
    
    class Meta:
        app_label = 'deposito'
        db_table = 'cre_extracto_deposito'
        verbose_name = "Extracto Deposito"
        verbose_name_plural = "Extractos Depositos"
        
        