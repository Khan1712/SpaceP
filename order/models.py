from decimal import Decimal

from django.db import models

# Create your models here.
from product.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, quantity, price):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': price
            }
            self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)] ['product'] = product

        for item in self.cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart)

    def get_total_price(self):
        return sum(Decimal(item['price'] * item['quantity']) for item in self.cart.values())

    def increment_quantity(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] < 20:
                self.cart[product_id]['quantity'] += 1
                self.save()




# Создать модели Cart, CartItem
# Сделать оформление заказа
# Отправлять инвойс на почту

