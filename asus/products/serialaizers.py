from rest_framework import serializers
from .models import *


# category with fewer fields
class CustomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['name']


class ProductFeaturesSerializer(serializers.ModelSerializer):
    feature = FeatureSerializer(read_only=True)

    class Meta:
        model = ProductFeatures
        fields = ['describe', 'feature']


class CategorySerializer(serializers.ModelSerializer):
    sub = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'sub']

    def get_sub(self, obj: Category):
        # get child of each object
        return CategorySerializer(obj.children, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    category = CustomCategorySerializer(read_only=True, many=True)
    features = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = '__all__'

    def get_features(self, obj: Products):
        # get features of each object
        return ProductFeaturesSerializer(obj.features, many=True).data
