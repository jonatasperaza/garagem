from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Acessorio, Cor, Modelo


class Veiculo(models.Model):

    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        verbose_name=_('Modelo'),
    )
    cor = models.ForeignKey(
        Cor,
        on_delete=models.CASCADE,
        verbose_name=_('Cor'),
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
    acessorio = models.ManyToManyField(
        Acessorio,
        blank=True,
        verbose_name=_("Acessórios"),
    )

    def __str__(self):
        return f'{self.id} - {self.cor} - {self.cor} - {self.ano}'
