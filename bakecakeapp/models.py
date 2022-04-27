from django.db import models


class Level(models.Model):
    amount = models.IntegerField(default=1, verbose_name="Количество уровней")
    price = models.IntegerField("Цена")

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name = "Количество уровней"
        verbose_name_plural = "Количество уровней"


class Form(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Формы"


class Topping(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Топпинг"
        verbose_name_plural = "Топпинг"


class Berry(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ягода"
        verbose_name_plural = "Ягоды"


class Decor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Декор"
        verbose_name_plural = "Декор"
