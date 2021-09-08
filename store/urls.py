
from django.contrib import admin
from django.urls import path
from .views import index
from .views import shop
from .views import shopps
urlpatterns = [
    path('', index),
    path('shopps',views.shopps,name="shopps"),
]
