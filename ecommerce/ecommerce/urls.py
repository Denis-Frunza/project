"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
    path('cartitem/', views.ListCart.as_view(), name='list-cartitem'),
    path('cartitem/create/<int:pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-item-from-cart/<int:pk>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls'))
]
