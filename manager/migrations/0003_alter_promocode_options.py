# Generated by Django 4.0.4 on 2022-04-30 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_promocode_order_promocode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promocode',
            options={'verbose_name': 'Промокод', 'verbose_name_plural': 'Промокоды'},
        ),
    ]