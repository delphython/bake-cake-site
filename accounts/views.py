from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from manager.models import Order
from .forms import LoginForm, RegistrationForm


@login_required
def show_lk(request):
    orders = (
        Order.objects.prefetch_related()
        .select_related()
        .filter(customer__id=request.user.id)
    )
    return render(
        request,
        "accounts/lk.html",
        context={"user": request.user, "orders": orders},
    )


class LoginUser(auth_views.LoginView):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "accounts/login.html", context={"form": form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("lk")
            return redirect("login")


class LogoutUser(auth_views.LogoutView):
    next_page = reverse_lazy("login")


class UserCreateView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/registration.html"

    def __init__(self):
        self.object = None

    def get_success_url(self):
        return reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("lk")
