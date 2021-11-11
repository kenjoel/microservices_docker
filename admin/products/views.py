import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, User
from .producer import publish
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish("Products List", serializer.data)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("Product Added", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        item = Products.objects.get(id=pk)
        found = ProductSerializer(item, many=False)
        return Response(found.data)

    def update(self, request, pk=None):
        item = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=item, data=request.data)
        serializer.is_valid()
        serializer.save()
        publish("Product Updated", serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        item = Products.objects.get(id=pk)
        if item:
            item.delete()
            publish("Product Destroyed", pk)
        else:
            return "No such item"
        return Response(status=status.HTTP_204_NO_CONTENT)

    def exterminate(self, request):
        items = Products.objects.all()
        items.delete()
        return Response(status=status.HTTP_410_GONE)







class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "id": user.id
        })
