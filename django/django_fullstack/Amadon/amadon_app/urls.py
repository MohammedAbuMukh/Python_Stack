from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('checkout', views.checkout, name='checkout'),
]