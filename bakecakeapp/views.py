from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view


def index(request):
    return render(request, "bakecakeapp/index.html")


def lk(request):
    return render(request, "bakecakeapp/lk.html")


@csrf_protect
@api_view(["POST"])
def register_order(request):
    print(request.data)
    return render(request, "bakecakeapp/payments.html")
