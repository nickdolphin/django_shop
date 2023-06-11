from django import forms
from django.contrib.auth.models import User

from .models import Product


class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            'title',
            'text',
            'price',
            'cat',
        }
