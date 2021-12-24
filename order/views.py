from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from order.forms import AddToCartForm
from order.models import Cart, Order, OrderItem
from product.models import Product


class AddToCartView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            quantity = data.get('quantity')
            cart.add(product.id, quantity, str(product.price))
        return redirect(reverse_lazy('cart-details'))


class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product.id)
        return redirect(reverse_lazy('cart-details'))


class CartDetailsView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart_details.html', {'cart': cart})


class IncrementQuantityView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.increment_quantity(product.id)
        return redirect(reverse_lazy('cart-details'))


class CreateOrderView(View):
    def get(self, request):
        session_cart = Cart(request)
        if not session_cart.cart:
            return redirect(reverse_lazy('index'))
        order = Order(user=request.user, total_price=session_cart.get_total_price())
        for id, values in session_cart.cart.values():
            product = Product.objects.get(id=id)
            OrderItem(order=order, product=product, quantity=values.get('quantity'))
        session_cart.clean()
        order.send_activation_mail()


class ActivateOrderView(View):
    def get(self, request, activation_Code):
        order = Order.objects.get(user=request.user, activation_Code=activation_Code)
        order.is_active = True
        order.save()
        order.send_mail()


