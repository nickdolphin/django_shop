from django.contrib import admin
from django.urls import path, include

from .views import home_page, product_detail, all_posts_category, add_product, delete_product, show_basket, \
    add_to_basket, clear_basket, delete_from_basket, order, user_orders

urlpatterns = [
    path('', home_page, name='home'),
    path('shop/detail/<int:product_id>', product_detail, name='product_detail'),
    path('shop/category/<int:category_id>', all_posts_category, name='category'),
    path('shop/add', add_product, name='add_product'),
    path('shop/delete/<int:product_id>', delete_product, name='delete_product'),
    path('shop/basket', show_basket, name='show_basket'),
    path('shop/basket/<int:product_id>', add_to_basket, name='add_to_basket'),
    path('shop/clear', clear_basket, name='clear_basket'),
    path('shop/basket/delete<int:product_id>', delete_from_basket, name='delete_from_basket'),
    path('shop/order', order, name='order'),
    path('shop/order_history', user_orders, name='user_orders'),
]