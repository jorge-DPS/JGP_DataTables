# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from location_field.models.plain import PlainLocationField

from apps.contrib.utils.files import clean_static_url
from apps.contrib.utils.strings import get_uuid5


class Sucursal(models.Model):
    """Sucursal model."""
    slug = models.SlugField(
        verbose_name=_("Slug"),
        default=get_uuid5,
        db_index=True,
        unique=True,
    )
    nombre = models.CharField(
        verbose_name=_('Nombre'),
        max_length=100,
    )
    direccion = models.TextField(
        verbose_name=_('direccion'),
    )
    telefono = models.CharField(
        verbose_name=_('Telefono/Celular'),
        max_length=15,
        blank=True, null=True,
    )    
    punto_gps = PlainLocationField(
        based_fields=['La Paz'],
        zoom=7,
        default='-16.510659, -68.141776',
        verbose_name=_("Punto GPS"),
        blank=True, null=True,
    )
    foto = models.ImageField(
        verbose_name=_('Fotografia'),
        upload_to ='sucursales/%Y%m%d/',
        blank=True, null=True,
    )


    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.nombre is None or self.nombre.strip() == '':
            self.nombre = self.slug
        super().save(*args, **kwargs)

    @property
    def get_telefono(self):
        return self.telefono

    @property
    def foto_url(self):
        return clean_static_url(self.foto.url) if self.foto else None

    class Meta:
        db_table = 'sucursal'
        verbose_name = _('Sucursal')
        verbose_name_plural = _('Sucursales')
        app_label = 'empresa'
