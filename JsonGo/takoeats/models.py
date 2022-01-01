from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime

import os
import hashlib
import json

def hash_img(instance, filename):
    instance.image.open()
    content = instance.image.read()
    _, ext = os.path.splitext(filename)
    return f'item_images/{hashlib.sha256(content).hexdigest()}{ext}'

class User(models.Model):
    display_name = models.CharField(max_length=16, null=False)
    user_entity = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
            return self.user_entity.username

class Shop(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
    name = models.CharField(max_length=16)
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to=hash_img, blank=True, null=True)

    def __str__(self):
            return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=16)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
            return self.name

class Item(models.Model):
    ITEM_STATUS = (
        (0, '上架中'),
        (1, '已下架'),
        (2, '已刪除'),
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(choices=ITEM_STATUS, default=1)
    category = models.ForeignKey(ItemCategory, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=hash_img, null=True)
    desc = models.CharField(max_length=100, null=True)

    def __str__(self):
            return json.dumps({'id': self.id, 'name': self.name, 'price': float(self.price), 'status': self.status, 'category': self.category.name})


class Order(models.Model):
    STATUS_CHOICES = (
        (1, '準備中'),
        (2, '等待外送'),
        (3, '外送中'),
        (4, '外送員已到達目的地'),
        (5, '完成'),
        (6, '取消'),
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cutomer")
    delivery = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="delivery")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    order_time = models.TimeField(default=timezone.now)
    price_sum = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=100)

    def __str__(self):
                return str(self.order_id), str(self.price_sum)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
                    return str(self.items), str(self.quantity)

