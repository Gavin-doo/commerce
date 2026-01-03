from django.urls import path
from .views import CartListCreateView, CartDetailView

urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
]