from django.db import models
from Account.models import User_create
from flat.models import Flat
from django.conf import settings
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='flat_item')
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'

    def get_total(self):
        total = self.item.flat_rent * self.quantity
        float_total = format(total, '0.2f')
        return float_total


class Order(models.Model):
    order_items = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=265, blank=True, null=True)
    OrderId = models.CharField(max_length=200, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.order_items.all():
            total = total + float(order_item.get_total())

        return total


