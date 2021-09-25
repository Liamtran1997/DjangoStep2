from django.db import models
from cart.models import Cart
# Create your models here.

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=False)
    description = models.TextField(default='')
    is_deleted = models.BooleanField(default=False)