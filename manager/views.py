from django.shortcuts import render

from .models import Order


def view_orders(request):
    orders = Order.objects.select_related().filter(
        customer__id=request.user.id
    )

    return render(
        request,
        template_name="bakecakeapp/lk-order.html",
        context={
            "orders": orders,
        },
    )
