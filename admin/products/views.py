from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from admin.products.models import Products
from admin.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
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
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        item = Products.objects.get(id=pk)
        if item:
            item.delete()
        else:
            return "No such item"
        return Response(item.data, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    pass

