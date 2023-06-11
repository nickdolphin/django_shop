from django.contrib import admin
from .models import Product, Category, Basket, Order

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(Order)

