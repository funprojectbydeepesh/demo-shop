from django.shortcuts import render, redirect , get_object_or_404
from .models import Cart, CartItem
from shop.models import Product


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    
    return cart

def add_cart(request, product_id):
    pass
