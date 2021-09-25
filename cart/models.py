from django.db import models
from user.models import User
from product.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False)
    time = models.DateTimeField(auto_now=True)
    total = models.IntegerField(default=0, null=False)
    is_status = models.BooleanField(default=False)