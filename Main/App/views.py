from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *


class ProductApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        return Response({'products': ProductSerializer(products, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'product': serializer.data}, status=201)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Product.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        serializer = ProductSerializer(data=request.data, instance=instance)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'product': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            product = Product.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        product.delete()

        return Response({'product': 'delete post' + product.name})


class ManufacturerApiView(APIView):

    def get(self, request, *args, **kwargs):
        print(kwargs)
        pk = kwargs.get('pk', None)
        if not pk:
            manufacturers = Manufacturer.objects.all()
            return Response({'manufacturers': ManufacturerSerializer(manufacturers, many=True).data})
        try:
            manufacturer = Manufacturer.objects.get(id=pk)
            return Response({'manufacturer': ManufacturerSerializer(manufacturer, many=False)})
        except:
            return Response({'error': 'Object does not exit'})

    def post(self, request):
        serializer = ManufacturerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'manufacturer': serializer.data}, status=201)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Manufacturer.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        serializer = ManufacturerSerializer(data=request.data, instance=instance)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'manufacturer': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            manufacturer = Manufacturer.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        manufacturer.delete()
        return Response({'manufacturer': 'delete post' + manufacturer.name})


class CategoryApiView(APIView):
    def get(self, request):
        categorys = Category.objects.all()
        return Response({'categorys': CategorySerializer(categorys, many=True).data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'category': serializer.data}, status=201)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Category.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        serializer = CategorySerializer(data=request.data, instance=instance)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'category': serializer.data})

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            category = Category.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exit'})

        category.delete()
        return Response({'category': 'delete post' + category.name})
