from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ('category',)



@admin.register(ProductFeatures)
class ProductFeaturesAdmin(admin.ModelAdmin):
    list_display = ['product', 'feature', 'describe']
