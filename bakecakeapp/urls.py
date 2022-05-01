from django.conf.urls.static import static
from django.urls import include, path

from django.conf import settings
from . import views
from manager.views import view_orders


urlpatterns = [
    path("", views.index, name="index"),
    path("lk/", views.lk),
    path("lk_order/", view_orders),
    path("order/", views.register_order),
    path("payment/", include("payment.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
