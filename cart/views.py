from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal, ROUND_HALF_UP

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def cart(request, quantity=0, cart_item=None, vat=0, total=0, after_vat_price=0):
    print("Cart view called")  # Debugging statement
    cart_items = []
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        print(f"Cart found: {cart}")  # Debugging statement
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.new_price * cart_item.quantity)
            quantity += cart_item.quantity

    except ObjectDoesNotExist:
        print("Cart does not exist")  # Debugging statement
        pass

    total = Decimal(total)

    # Calculate VAT using Decimal
    vat_rate = Decimal('0.13')
    vat = (total * vat_rate) / (1 + vat_rate)

    # Round VAT to 2 decimal places
    vat = vat.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    after_vat_price = total - vat

    context = {
        'total': total,
        'vat': vat,
        'after_vat_price': after_vat_price,
        'quantity': quantity,
        'cart_items': cart_items
    }

    return render(request, 'cart.html', context)


def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()

    return redirect('cart')


def reduce_cart_item(request, product_id):
    
    try:
        product = Product.objects.get(id = product_id)
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_item = CartItem.objects.get(cart= cart, product = product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('cart')


def remove_cart_item(request, product_id):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_item = CartItem.objects.get(cart = cart, product__id = product_id)
        if cart_item:
            cart_item.delete()
    except ObjectDoesNotExist:
        print('Objects not found')

    return redirect('cart')