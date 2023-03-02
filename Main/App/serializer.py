from rest_framework import serializers
from .models import *


# Мне было лень писать поля, поэтому использовал ModelSerializer. Все остальное по презентаци
class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance

    class Meta:
        fields = '__all__'
        model = Category


class ManufacturerSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()

        return instance

    class Meta:
        fields = '__all__'
        model = Manufacturer


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.price = validated_data.get('price', instance.price)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.category = validated_data.get('category', instance.category)

        instance.save()

        return instance

    class Meta:
        fields = '__all__'
        model = Product
