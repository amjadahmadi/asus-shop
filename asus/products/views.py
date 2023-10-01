from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serialaizers import *


class UserViewSet(ListCreateAPIView):
    """
    A viewset that provides the standard actions
    """
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer

class ProductViewSet(ListCreateAPIView):
    """
    A viewset that provides the standard actions
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer