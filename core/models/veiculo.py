from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Categoria, Cor, Marca


class Veiculo(models.Model):
    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        verbose_name=_("Marca"),
    )
    cor = models.ForeignKey(
        Cor,
        on_delete=models.CASCADE,
        verbose_name=_("Cor"),
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name=_("Categoria"),
    )
    ano = models.PositiveIntegerField(
        verbose_name=_("Ano"),
        null=True,
        blank=True,
        default=0
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Preço"),
        null=True,
        blank=True,
        default=0.00
    )

    def __str__(self):
        return f'{self.marca} - {self.categoria} - {self.ano} - {self.cor}'
