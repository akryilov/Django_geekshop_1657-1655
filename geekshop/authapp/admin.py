from django.contrib import admin

# Register your models here.
from authapp.models import User
from basket.admin import BasketAdmin
from basket.models import Basket


@admin.register(User)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    inLines = (BasketAdmin,)
