# -*- coding: utf-8 -*-
from django.db import models
from location_field.models.plain import PlainLocationField
from django.utils.translation import ugettext_lazy as _
from apps.contrib.utils.files import clean_static_url
from apps.contrib.utils.strings import get_uuid5
from apps.accounts.models.user import User
from apps.zona.models.localidad import Localidad
from apps.empresa.models.sucursal import Sucursal
from datetime import datetime


class Zona(models.Model):
    """Zona model."""
    
    descripcion = models.CharField(
        verbose_name=_('Descripcion de zona'),
        max_length=50,
        blank = False, null = False
    )
    localidad = models.ForeignKey(
        Localidad,
        on_delete=models.CASCADE,
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
        null = True,blank=True,
    )
    eliminado_en = models.DateTimeField(
        verbose_name=("Fecha Eliminacion"),
        null = True,blank=True,
    )
    
    
    def save(self, *args, **kwargs):
        self.descripcion = " ".join((self.descripcion).lower().capitalize().split())
        return super(Zona, self).save(*args, **kwargs)
    
    class Meta:
        app_label = 'zona'
        db_table = 'cli_tbl_zona'
        verbose_name = "Zona"
        verbose_name_plural = "Zonas" 
        unique_together = ('descripcion','localidad',)
    def str(self):
        return "%s " % (self.descripcion)
    

   