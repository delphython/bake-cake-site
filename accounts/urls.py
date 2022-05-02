from django.urls import path

from . import views


urlpatterns = [
    path("lk/", views.show_lk, name='lk'),
    path("login/", views.LoginUser.as_view(), name='login'),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
    path("registration/", views.UserCreateView.as_view(), name='registration'),
]
