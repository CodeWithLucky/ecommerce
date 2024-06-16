from django.contrib import admin
from . models import Cart, CartItem

# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'product', 
        'quantity',
        'cart',
        'is_active'
        
    ]

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart)