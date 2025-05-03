from django.db import models
from django.utils.translation import gettext_lazy as _


class Categoria(models.Model):
    """
    Modelo que representa uma categoria.
    """

    descricao = models.CharField(
        max_length=100,
        verbose_name=_("Descrição"),
    )

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')
        ordering = ["descricao"]

    def __str__(self):
        return self.descricao
