# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.core.validators import ProhibitNullCharactersValidator


class ArqueoConfig(AppConfig):
    """Configuration for users and permissions functionalties."""

    name = 'apps.procesos.arqueo'
    verbose_name = 'Arqueo'
    verbose_name_plural = 'Arqueos'

