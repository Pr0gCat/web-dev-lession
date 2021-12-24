from django.db import models
from django.conf import settings

class User(models.Model):
    user_entity = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.CharField(max_length=64)

    def __str__(self):
            return self.user_entity.username

class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
    name = models.CharField(max_length=16)
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
            return self.name


class Item(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField()

    def __str__(self):
            return self.name

class Order(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cutomer")
    delivery = models.OneToOneField(User, on_delete=models.CASCADE, related_name="delivery")
    status = models.IntegerField()
    order_time = models.TimeField()
    price_sum = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
            return self.id, self.delivery_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
            return self.id, self.item_id

