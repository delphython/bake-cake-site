from django.contrib import admin

from manager.models import Order, Promocode


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    pass
