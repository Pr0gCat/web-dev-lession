from django.contrib import admin

from .models import User, Shop, Item, ItemCategory, Order, OrderItem

# Register your models here.
admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
