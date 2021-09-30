from django.contrib import admin
from order.models import Order
from product.models import Product, Category
from cart.models import Cart
from .models import User_Detail
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class OrderForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Order
        fields = '__all__'

class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ["id", "cart", "address", "description", "is_deleted"]
    search_fields = ["cart", "address"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "unit", "is_deleted"]
    search_fields = ["name"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_deleted"]
    search_fields = ["name"]
    list_filter = ["name"]

# class CartAdmin(admin.ModelAdmin):
#     list_display = ["id", "quantity", "time", "total", "is_status"]

class User_DetailAdmin(admin.ModelAdmin):
    list_display = ["id", "phone", "address", "gender", "fullname"]
    search_fields = ["phone", "gender", "address", "fullname"]


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart)
admin.site.register(User_Detail, User_DetailAdmin)
