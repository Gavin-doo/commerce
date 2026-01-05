from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart
from . models import Order, OrderItem
from . serializers import OrderSerializer

# Create your views here.

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    get_queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
        
        total = 0

        for item in cart_items:
            total += item.product.price * item.quantity

        order = Order.objects.create(user=request.user, total_price=total)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()  # Clear the cart after creating the order

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        print("LOG : Product list called from conflict-test-1")
        return super().get(request, *args, **kwargs)
    

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')