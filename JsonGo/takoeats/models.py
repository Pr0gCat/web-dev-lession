from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    display_name = models.CharField(max_length=16, null=False)
    user_entity = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
            return self.user_entity.username

class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
    name = models.CharField(max_length=16)
    rating_sum = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    shop_img = models.ImageField(upload_to='shop_img', blank=True)

    def __str__(self):
            return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
            return self.name

class Item(models.Model):
    ITEM_STATUS = (
        (0, '上架中'),
        (1, '已下架'),
        (2, '已刪除'),
    )
    shop_id = models.OneToOneField(Shop, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(choices=ITEM_STATUS, default=1)
    category = models.ForeignKey(ItemCategory, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='item_images', null=True)

    def __str__(self):
            return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        (1, '準備中'),
        (2, '等待外送'),
        (3, '外送中'),
        (4, '外送員已到達目的地'),
        (5, '完成'),
        (6, '取消'),
    )
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, related_name='shop')
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cutomer")
    delivery = models.OneToOneField(User, on_delete=models.CASCADE, related_name="delivery")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    order_time = models.TimeField(default=timezone.now)
    price_sum = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=100)

    def __str__(self):
            return self.id, self.delivery_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
            return self.id, self.item_id

