from django.urls import path, include
from .views import Indexclass,LoginClass,ViewUser,view_product
app_new = "login" #Namespace
urlpatterns = [
    # path('',Indexclass.as_view(), name="login"),
    path('', LoginClass.as_view(), name="login"),
    path('view/', ViewUser.as_view(), name="view"),
    path('view-product/', view_product, name="view-product"),
]