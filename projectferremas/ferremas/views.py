
from rest_framework import viewsets
from .models import Productos
from .serializers import ProductoSerializers
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializers


class PostsExternosView(APIView):
    def get(self, request):
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts')
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)