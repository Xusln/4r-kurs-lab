from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('dashbaord/', views.dashboard, name='dashboard'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('place-order/', views.place_order, name='place-order'),
    path('product-detail/', views.product_detail, name='product-detail'),
]
