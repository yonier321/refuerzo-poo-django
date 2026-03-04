from rest_framework import viewsets
from  .models import Proveedor, Producto, OrdenCompra,DetalleOrden
from .serializers import (
    ProveedorSerializer,
    ProductoSerializer,
    OrdenCompraSerializer,
    DetalleOrdenSerializer
)
# importaciones para manejar excepcion de no borrar producto con proveedor asociado
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ProtectedError


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(
                {"error": "No se puede eliminar el producto porque tiene detalles de orden asociados."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrdenCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer
    
    
class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer