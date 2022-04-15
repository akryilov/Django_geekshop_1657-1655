from django.contrib import admin

# Register your models here.

from basket.models import Basket

admin.site.register(Basket)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created', 'update_timestamp')
    readonly_fields = ('create_timestamp', 'update_timestamp')
    extra = 3
