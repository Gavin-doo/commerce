from rest_framework import generics, permissions
from .models import Cart
from .serializers import CartSerializer
from products.models import Products
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        quantity = self.request.data.get('quantity', 1)
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({"error": "Product does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = Cart.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        serializer.instance = cart_item

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)