from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('', CartDetailsView.as_view(), name='cart-details'),
    path('increment/<int:product_id>/', IncrementQuantityView.as_view(), name='increment_quantity'),
    path('create_order/', CreateOrderView.as_view(), name='create-order'),

]
