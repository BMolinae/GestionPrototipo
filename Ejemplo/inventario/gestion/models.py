from django.db import models

# gestion/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)

