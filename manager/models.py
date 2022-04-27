from django.db import models
from django.contrib.auth.models import User

from bakecakeapp.models import Level, Form, Berry, Decor, Topping


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        related_name="customers",
        verbose_name="Заказчик",
        on_delete=models.PROTECT,
    )
    level = models.ForeignKey(
        Level,
        verbose_name='Количество уровней',
        related_name='orders',
        on_delete=models.PROTECT,
    )
    form = models.ForeignKey(
        Form,
        verbose_name="Форма",
        related_name='orders',
        on_delete=models.PROTECT,
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name="Топпинг",
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    berry = models.ForeignKey(
        Berry,
        verbose_name="Ягоды",
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    decor = models.ForeignKey(
        Decor,
        verbose_name="Декор",
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    inscription = models.CharField("Надпись", max_length=200, blank=True)
    comment = models.TextField("Комментарий к заказу", blank=True)
    address = models.CharField("Адрес доставки", max_length=200)
    delivery_date = models.DateField(
        verbose_name="Дата доставки",
    )
    delivery_time = models.TimeField(
        verbose_name="Время доставки",
    )
    cost = models.IntegerField('Стоимость')
    status = models.CharField(
        'Статус заказа',
        max_length=20,
        default='new',
        choices=(('new', 'Необработанный'), ('processed', 'Обработан'),
                 ('cooking', 'Готовится'), ('ready', 'Готов'))
    )

    def __str__(self):
        return f"Заказ № {self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
