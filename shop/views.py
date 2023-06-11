from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Category, Product, Basket, Order


def popular_product():
    products = Product.objects.all()
    popular_products = {}
    for i in products:
        popular_products[i.title] = i.orders.all().count()
    return popular_products


def home_page(request):
    category = Category.objects.all()
    return render(request, 'shop/home_page.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


def all_posts_category(request, category_id):
    products = Product.objects.filter(cat_id=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'shop/category.html', {'products': products, 'category': category})


def add_product(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = datetime.now()
            product.published_date = datetime.now()
            product.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = PostForm()
    return render(request, 'shop/add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('home')


def show_basket(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    product = user_basket.product.all()
    final_price = 0
    for i in product:
        final_price += i.price
    return render(request, 'shop/user_basket.html', {'product': product, 'final_price': final_price})


def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user).first()
    if basket == None:
        basket = Basket.objects.create(user=request.user)
    basket.product.add(product)
    return redirect('product_detail', product_id=product.id)


def clear_basket(request):
    basket = Basket.objects.filter(user=request.user).first()
    basket.product.clear()
    return redirect('show_basket')


def delete_from_basket(request, product_id):
    basket = Basket.objects.filter(user=request.user).first()
    product = basket.product.remove(product_id)
    return redirect('show_basket')


def user_orders(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'shop/order.html', {'orders': orders})


def order(request):
    basket = Basket.objects.filter(user=request.user).first()
    products = basket.product.all()
    total_price = products.aggregate(Sum('price'))['price__sum']
    order = Order.objects.create(user=request.user, total_price=total_price)
    order.products.add(*products)

    basket.product.clear()
    return redirect('user_orders')
