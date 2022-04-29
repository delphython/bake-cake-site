from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views


urlpatterns = [
    path("", views.index),
    path("lk/", views.lk),
    path("order/", views.register_order),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
