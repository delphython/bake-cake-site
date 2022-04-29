from django.contrib import admin

from manager.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
