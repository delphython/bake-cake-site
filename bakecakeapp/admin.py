from django.contrib import admin

from bakecakeapp.models import Level, Form, Berry, Decor, Topping


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    pass


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    pass


@admin.register(Berry)
class BerryAdmin(admin.ModelAdmin):
    pass
