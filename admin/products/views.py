from django.contrib.auth.models import User
from knox.models import AuthToken
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .models import Products
from .producer import publish
from .serializers import ProductSerializer, UserSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish("Products List", serializer.data)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
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
        serializer.save(owner=self.request.user)
        publish("Product Updated", serializer.data)
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






class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"User":serializer.data, "status":status.HTTP_201_CREATED, "token":AuthToken.objects.create(
            serializer)[1]
            })

    def retrieve(self, request, pk=None):
        item = User.objects.get(id=pk)
        found = UserSerializer(item, many=False)
        return Response(found.data)

    def update(self, request, pk=None):
        item = User.objects.get(id=pk)
        serializer = UserSerializer(instance=item, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        item = User.objects.get(id=pk)
        if item:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return "No such item"

    def exterminate(self, request):
        items = User.objects.all()
        items.delete()
        return Response(status=status.HTTP_410_GONE)


