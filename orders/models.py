from django.db import models
from shop.models import *


class Order(models.Model):
    last_name = models.CharField(max_length=20, verbose_name='姓')
    first_name = models.CharField(max_length=20, verbose_name='名')
    email = models.EmailField(max_length=50, verbose_name='邮箱地址')
    address = models.CharField(max_length=200, verbose_name='收货地址')
    postal_code = models.CharField(max_length=20, verbose_name='邮政编码')
    city = models.CharField(max_length=100, verbose_name='城市')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新')
    paid = models.BooleanField(default=False, verbose_name='已付款')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='订单')
    product = models.ForeignKey(Product, related_name='order_items', verbose_name='产品名称')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='产品价格')
    quantity = models.PositiveIntegerField(default=1, verbose_name='数量')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
