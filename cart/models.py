from django.db import models
from django.utils.translation import gettext_lazy as _ 
from shop.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=200, verbose_name=_('Cart Id'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.cart_id}'
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('Cart'))
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))


    def __str__(self):
        return f'{self.product.name}'
    
    def calculate_total_price(self):
        return f'{self.product.price}' * f'{self.quantity}'
