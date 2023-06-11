from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    published_date = models.DateTimeField(verbose_name='дата добавления', auto_now=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='product_basket')

    def __str__(self):
        return f'{self.user}'


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.products}'
