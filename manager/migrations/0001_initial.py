# Generated by Django 4.0.4 on 2022-04-27 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bakecakeapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscription', models.CharField(blank=True, max_length=200, verbose_name='Надпись')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий к заказу')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес доставки')),
                ('delivery_date', models.DateField(verbose_name='Дата доставки')),
                ('delivery_time', models.TimeField(verbose_name='Время доставки')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('status', models.CharField(choices=[('new', 'Необработанный'), ('processed', 'Обработан'), ('cooking', 'Готовится'), ('ready', 'Готов')], default='new', max_length=20, verbose_name='Статус заказа')),
                ('berry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='bakecakeapp.berry', verbose_name='Ягоды')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
                ('decor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='bakecakeapp.decor', verbose_name='Декор')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='bakecakeapp.form', verbose_name='Форма')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='bakecakeapp.level', verbose_name='Количество уровней')),
                ('topping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='bakecakeapp.topping', verbose_name='Топпинг')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
