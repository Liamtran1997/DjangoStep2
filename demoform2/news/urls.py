from django.urls import path
from .import views
app_name = "news" #Namespace
urlpatterns = [
    path('',views.IndexClass.as_view(),name="index"), # URL for Class Base View
    # path('', views.index, name="index"),
    # path('add/', views.PostClass.as_view(), name="add"), # URL for Class Base View
    path('save/', views.ClassSaveView.as_view(), name="save"), # URL for Class Base View
    path('email/', views.email_view, name="email"), # URL for Function Base View
    path('process/', views.process, name="process"),
]
