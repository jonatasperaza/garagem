from django.db import models
from django.utils.translation import gettext_lazy as _


class Marca(models.Model):
    """
    Modelo que representa uma marca.
    """

    nome = models.CharField(
        max_length=100,
        verbose_name=_('Nome'),
    )
    nacionalidade = models.CharField(
        max_length=100,
        verbose_name=_("Nacionalidade"),
    )

    class Meta:
        verbose_name = _("Marca")
        verbose_name_plural = _("Marcas")
        ordering = ["nome"]

    def __str__(self):
        return self.nome.upper()
