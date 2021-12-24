from decimal import Decimal

from django.contrib.admin import action
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
from django.utils.crypto import get_random_string

from product.models import Product

User = get_user_model()

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

    def clean(self):
        for product_id in self.cart:
            self.remove(product_id)

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


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField()
    activation_code = models.CharField(max_length=8, blank=True, null=True)

    def create_activation_code(self):
        code = get_random_string(8)
        self.activation_code = code
        self.save()

    def send_activation_mail(self):
        self.create_activation_code()
        message = f'http://localhost:8000/account/activate/{self.activation_code}/'
        send_mail(
            'Подтверждение заказа',
             message,
            'test@gmail.com',
            [self.user.email]
        )

    def send_mail(self):
        if self.is_active:
            message = 'Ваш заказ принят'
            send_mail(
                'Заказ',
                message,
                'test@gmail.com',
                [self.user.email]
            )
        else:
            message = 'Ваш заказ не подтвержден. Пожалуйста, подтвердите заказ.'
            send_mail(
                'Заказ',
                message,
                'test@gmail.com',
                [self.user.email]
            )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(validators=[MaxValueValidator(20)])


# Создать модели Cart, CartItem
# Сделать оформление заказа
# Отправлять инвойс на почту

