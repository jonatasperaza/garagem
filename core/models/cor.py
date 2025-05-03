from django.db import models
from django.utils.translation import gettext_lazy as _


class Cor(models.Model):
    """
    Modelo que representa uma cor.
    """

    descricao = models.CharField(
        max_length=100,
        verbose_name=_("Descrição"),
    )

    class Meta:
        verbose_name = _("Cor")
        verbose_name_plural = _("Cores")
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao
