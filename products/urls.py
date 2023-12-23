from django.urls import path,include

from .views import ProductList,ProductDetail,subscriptions
from .views import ProductCreate

urlpatterns = [
    path('', ProductList.as_view(), name = 'product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name = 'product_detail'),
    path('subscriptions/', subscriptions, name='subscriptions')
]