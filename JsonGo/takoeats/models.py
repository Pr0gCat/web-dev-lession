from django.db import models

class Status(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
            return self.type


class Users(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    created_on = models.DateField(max_length=64)
    def __str__(self):
            return self.username


class Shops(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64)
    rating = models.DecimalField(decimal_places=1,max_digits=2)
    rating_count = models.IntegerField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
            return self.name


class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    shop_id = models.ForeignKey(Shops, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    available = models.BooleanField()
    def __str__(self):
            return self.name


class Orders(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    customer = models.CharField(max_length=64)
    delivery_id = models.CharField(max_length=64)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    order_time = models.TimeField()
    def __str__(self):
            return self.id, self.delivery_id


class OrderItems(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=64)
    item_price = models.IntegerField()
    quantity = models.IntegerField()
    def __str__(self):
            return self.id, self.item_id






