from .views import ProductViewSet, UserViewSet
from django.urls import path

urlpatterns = [
    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'delete': 'exterminate'
    })),

    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'

    })),

    path('user/', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'delete': 'exterminate'
    })),

    path('products/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'

    })),
]
