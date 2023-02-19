from django.contrib import admin
from order.models import Cart, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'paymentId', ' OrderId', 'created']
    list_filter = ('OrderId', 'paymentId',)

    class Meta:
        models = Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)

