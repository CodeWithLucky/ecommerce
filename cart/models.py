from django.db import models
from product.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(blank=True, max_length=255)
    date_added = models.DateTimeField(null=True,blank=True, auto_now_add=False)

    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.new_price * self.quantity

    def __unicode__(self):
        return self.product