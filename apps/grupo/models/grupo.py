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


class Grupo(models.Model):
    """grupo solidario model."""
    codigo_grupo = models.AutoField(auto_created=True, primary_key=True)  
    descripcion_grupo = models.CharField(
        verbose_name=_('Descripcion de grupo solidario'),
        max_length=50,
        unique=True,
        blank = False, null = False 
    )
    
    secuencia_grupo = models.SmallIntegerField(
        verbose_name=_('secuencia_grupo'),
        blank = False, null = False,
        default = 0
        
    )
    ultima_operacion = models.BigIntegerField(
        verbose_name=_('ultima_operacion'),
        blank = False, null = False,
        default = 0
        
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
        self.descripcion_grupo = " ".join((self.descripcion_grupo).lower().capitalize().split())
        return super(Grupo, self).save(*args, **kwargs)
    
    def str(self):
        return "%s " % (self.descripcion_grupo)
    
    class Meta:
        app_label = 'grupo'
        db_table = 'cli_tbl_grupos_solidarios'
        verbose_name = "Grupo solidario"
        verbose_name_plural = "Grupos solidarios"