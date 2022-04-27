from django.shortcuts import render


def index(request):
    return render(request, 'bakecakeapp/index.html')


def lk(request):
    return render(request, 'bakecakeapp/lk.html')
