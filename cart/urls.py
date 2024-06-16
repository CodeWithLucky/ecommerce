from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('reduce_cart_item/<int:product_id>/', views.reduce_cart_item, name="reduce_cart_item"),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
]
