from django.urls import path, include
from rest_framework import routers
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [

                  path('category/', UserViewSet.as_view(), name='category'),
                  path('products/', ProductViewSet.as_view(), name='products'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
