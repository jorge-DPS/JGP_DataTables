
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

EXTENCION_CARNET = (
    ("CH", _("CH")),
    ("LP", _("LP")),
    ("SC", _("SC")),
    ("CB", _("CB")),
    ("OR", _("OR")),
    ("TA", _("TA")),
    ("PO", _("PO")),
    ("BE", _("BE")),
    ("PA", _("PA")),
    ("SE", _("Sin Extencion")),
)
class Persona(models.Model):
    primer_nombre = models.CharField(
        verbose_name=_("Primer Nombre"),
        max_length=30,
        null=False, blank=False,
    )
    segundo_nombre = models.CharField(
        verbose_name=_("Segundo Nombre"),
        max_length=30,
        null=True, blank=True,
    )
    primer_apellido = models.CharField(
        verbose_name=_("Primer Apellido"),
        max_length=30,
        null=False,blank=False,
    )
    segundo_apellido = models.CharField(
        verbose_name=_("Segundo Apellido"),
        max_length=30,
        null=True, blank=True,
    )
    apellido_esposo = models.CharField(
        verbose_name=_("Apellido Esposo"),
        max_length=30,
        null=True, blank=True,
    )
    valor_documento_identificacion = models.CharField(
        verbose_name=_("Cedula de Identidad"),
        max_length=20,unique=True,
        null=False, blank=False,
    )
    complemento = models.CharField(
        verbose_name=_("Complemento"),
        max_length=20,
        null=True, blank=True,
    )
    extension = models.CharField(
        max_length = 2,
        verbose_name = _("Extension de documento de identidad"),
        help_text = _("Extension de documento de identidad"),
        choices = EXTENCION_CARNET,
        null=False, blank=False,
    )
    usuario_actualizacion = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name = _("Usuario_Actualizacion"),
        related_name="usuario_actualizacion_user",
        null=False, blank=False,
    )
    sucursal_creacion = models.ForeignKey(
        'empresa.Sucursal',
        on_delete=models.CASCADE,
        verbose_name = _("Sucursal_Creacion"),
        related_name="sucursal_creacion_sucursal",
        null=False, blank=False,
    )
    creado_en = models.DateTimeField(
        auto_now_add=True,
        null=False, blank=False,
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        null=False, blank=False,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=_("Fecha Eliminacion"),
        null=True, blank=True,
    )

    @property
    def get_nombre_completo(self):
        if self.segundo_nombre == None:
            self.segundo_nombre = ""

        if self.segundo_apellido == None:
            self.segundo_apellido = ""

        if self.apellido_esposo == None:
            self.apellido_esposo = ""
        else: 
            self.apellido_esposo = " de " + self.apellido_esposo 

        nombre_completo = self.primer_nombre +" " + self.segundo_nombre + " " + self.primer_apellido + " " + self.segundo_apellido + " " + self.apellido_esposo
        nombrec=str(nombre_completo)
        return nombrec

    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        db_table = "adm_tbl_persona"
        verbose_name = _("Persona")
        verbose_name_plural = _("Personas")
        permissions = (
            ('listar_todo_personas','Puede listar todas las personas'),
        )