
from rest_framework import viewsets
from .models import Productos
from .serializers import ProductoSerializers
from django.shortcuts import render

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializers


def productos_page(request):
    return render(request, 'ferremas/home.html')
