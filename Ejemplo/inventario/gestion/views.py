from django.shortcuts import render

# gestion/views.py
from rest_framework import viewsets
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

