from django.urls import path
from . import views


urlpatterns = [path("", views.index), path("lk/", views.lk)] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
