from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
#from .forms import PostForm
from .models import Category, Product, Basket, Order

def home_page(request):
    category = Category.objects.all()
    return render(request, 'shop/home_page.html')
