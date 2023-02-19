# -*- coding: utf-8 -*-

# Built in

from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

from apps.contrib.utils.files import clean_static_url


REQUIRED_FIELDS = getattr(settings, "PROFILE_REQUIRED_FIELDS", ["email"])


class   User(AbstractUser):
    """Represents the user of the platform."""

    USERNAME_FIELD = "username"

    username = models.CharField(
        _("Username"),
        max_length=50,
        unique=True,
        help_text=_(
            "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[
            validators.RegexValidator(
                r"^[\w.@+-]+$",
                _(
                    "Enter a valid username. This value may contain only "
                    + "letters, numbers and @/./+/-/_ characters.",
                ),
            ),
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        db_index=True,
    )

    email = models.EmailField(
        _("Correo electónico"),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
        unique=True,
        max_length=140,
        db_index=True,
    )

    code = models.IntegerField(
        _("Código de usuario"),
        error_messages={
            "unique": _("A user with that user code already exists."),
        },
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        unique=True, blank=True,
        null=True,
        # db_index=True,
    )

    first_name = models.CharField(
        verbose_name=_("Nombres"),
        max_length=100,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        verbose_name=_("Apellidos"),
        max_length=150,
        blank=True,
        null=True,
    )

    avatar = ProcessedImageField(
        verbose_name=_("Fotografia"),
        upload_to="profiles/%Y/%m/%d",
        processors=[ResizeToFill(350, 350)],
        format="PNG",
        options={"quality": 80},
        blank=True,
        null=True,
    )

    birthdate = models.DateField(
        verbose_name=_("fecha de nacimiento"),
        blank=True,
        null=True,
    )

    phone = models.CharField(
        verbose_name=_("Telefono/Celular"),
        max_length=15,
        blank=True,
        null=True,
    )

    incorporation_date = models.DateField(
        verbose_name=_("fecha de incorporación a la empresa"),
        blank=True,
        null=True,
    )

    lang = models.CharField(
        verbose_name=_("Language"),
        choices=settings.LANGUAGES,
        max_length=7,
        default="es",
        blank=True,
        null=True,
    )

    branch_office = models.ForeignKey(
        "empresa.Sucursal",
        verbose_name=_("Sucursal"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    role = models.ForeignKey(
        "empresa.Rol",
        verbose_name=_("Rol"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return "%s" % (self.code)

    def save(self, *args, **kwargs):
        if self.username is None or self.username.strip() == "":
            self.username = self.email
        super().save(*args, **kwargs)

    def change_password(self, new_password):
        self.set_password(new_password)
        self.save()

    @property
    def get_phone(self):
        return self.phone

    @property
    def full_name(self):
        full_name = "{0} {1}".format(self.first_name, self.last_name)
        return full_name.strip()

    @property
    def avatar_url(self):
        return clean_static_url(self.avatar.url) if self.avatar else None

    @property
    def recipient_name(self):
        if self.first_name:
            return self.first_name
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        app_label = "accounts"


"""
@receiver(pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).avatar
    except sender.DoesNotExist:
        return False
    new_file = instance.avatar
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
"""
