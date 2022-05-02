from django.contrib import admin

from manager.models import Order, Promocode
from payment.models import Payment


class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]
    list_display = ('id', 'get_payment', 'status', 'address',
                    'delivery_date', 'delivery_time')

    @admin.display(ordering='payments__status', description='Payment')
    def get_payment(self, obj):
        if obj.payments.first():
            return obj.payments.first().status


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    pass
