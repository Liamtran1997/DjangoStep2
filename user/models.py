from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_deleted = models.BooleanField(default=False)


class User_Detail(models.Model):
    class Meta:
        ordering = ["id"]
    set_gender = (0, "Female"), (1, "Male")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(default='', max_length=15)
    address = models.CharField(max_length=100)
    gender = models.IntegerField(choices=set_gender, default=0)
    fullname = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname