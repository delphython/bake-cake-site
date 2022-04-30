from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer

from manager.models import Order, Promocode
from .models import Level, Form, Topping, Berry, Decor


def index(request):
    return render(request, "bakecakeapp/index.html")


def lk(request):
    return render(request, "bakecakeapp/lk.html")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "inscription",
            "comment",
            "address",
            "delivery_date",
            "delivery_time",
            "cost",
        ]


@csrf_protect
@api_view(["POST", "GET"])
def register_order(request):
    selected_cake = request.data
    # serializer = OrderSerializer(data=selected_cake)
    # serializer.is_valid(raise_exception=False)

    cake_level = Level.objects.filter(amount=selected_cake["Levels"])
    cake_form = Form.objects.filter(name=selected_cake["Form"])
    cake_topping = Topping.objects.filter(name=selected_cake["Topping"])
    cake_berry = Berry.objects.filter(name=selected_cake["Berries"])
    cake_decor = Decor.objects.filter(name=selected_cake["Decor"])

    customer = User.objects.filter(email=selected_cake["Email"])
    if not customer:
        customer = [
            User.objects.create_user(
                selected_cake["Name"], selected_cake["Email"], "11111111"
            )
        ]

    order = Order.objects.create(
        customer=customer[0],
        level=cake_level[0],
        form=cake_form[0],
        topping=cake_topping[0],
        berry=cake_berry[0],
        decor=cake_decor[0],
        inscription=selected_cake["Words"],
        comment=selected_cake["DelivComments"],
        address=selected_cake["Address"],
        delivery_date=selected_cake["Dates"],
        delivery_time=selected_cake["Time"],
        cost=selected_cake["Cost"],
    )
    if Promocode.objects.filter(code=selected_cake['Promocode']).first():
        promocode = Promocode.objects.get(code=selected_cake['Promocode'])
        order.promocode = promocode
        order.save()

    # return redirect("payment", order_id=order.id)
    return HttpResponseRedirect(f"/payment/{order.id}")
