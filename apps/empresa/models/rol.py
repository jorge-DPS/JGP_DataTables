# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.contrib.utils.strings import get_uuid5


class Rol(models.Model):
    """Role model."""

    slug = models.SlugField(
        verbose_name=_("Slug"),
        default=get_uuid5,
        db_index=True,
        unique=True,
    )
    codigo = models.CharField(
        verbose_name=_("codigo"),
        max_length=5,
    )
    nombre = models.CharField(
        verbose_name=_("Nombre"),
        max_length=50,
    )
    descripcion = models.TextField(
        verbose_name=_("direccion"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre

    @property
    def get_codigo(self):
        return self.codigo

    class Meta:
        db_table = "rol"
        verbose_name = _("Rol")
        verbose_name_plural = _("Roles")
        app_label = "empresa"


"""
class RolUser(models.Model):

    user = models.ForeignKey(
        "accounts.User",
        verbose_name=_("Usuario"),
    )
    rol = models.ForeignKey("Rol", verbose_name=_("Rol"))

    descripcion = models.TextField(
        verbose_name=_("Descripción"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nombre

    @property
    def get_nombre(self):
        return self.nombre

    class Meta:
        db_table = "rol"
        verbose_name = _("Rol")
        verbose_name_plural = _("Roles")
        app_label = "empresa"

"""
