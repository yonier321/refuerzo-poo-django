from django.contrib import admin
from django.contrib import admin
from .models import Proveedor, Producto, OrdenCompra, DetalleOrden

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(OrdenCompra)
admin.site.register(DetalleOrden)

# Register your models here.
