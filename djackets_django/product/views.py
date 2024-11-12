from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class LatestProductsList(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:4]

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)

        return Response(serializer.data)
