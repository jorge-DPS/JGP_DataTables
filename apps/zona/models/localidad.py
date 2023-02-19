# -*- coding: utf-8 -*-

from tabnanny import verbose
from django.db import models
from django.utils.translation import ugettext_lazy as _

from location_field.models.plain import PlainLocationField

from apps.contrib.utils.files import clean_static_url
from apps.contrib.utils.strings import get_uuid5

from apps.accounts.models.user import User
from apps.empresa.models.sucursal import Sucursal

#****django filtro de inicio rapido
from django_filters import filters
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.filters import GlobalFilter



class Localidad(models.Model):
    """Localidad model."""
    descripcion = models.CharField(
        verbose_name=_('Descripción Localidad'),
        max_length=50,
        blank = False, null = False
    )
    codigo_departamento = models.CharField(
        verbose_name=_('codigo_departamento'),
        max_length=2,
        blank = False, null = False
        
    )
    codigo_localidad = models.CharField(
        verbose_name=_('codigo_localidad'),
        max_length=2,
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
        verbose_name=("Fecha de creacion"),
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
   
    class Meta:
        app_label = 'zona'
        db_table = 'cli_tbl_localidad'
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades" 
        
    def __str__(self):
        return "%s" % (self.descripcion)


    
    