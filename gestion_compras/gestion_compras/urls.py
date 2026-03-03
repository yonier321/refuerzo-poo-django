#swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Gestión de Compras",
        default_version='v1',
        description="Documentación de la API del sistema de compras",
        contact=openapi.Contact(email="yonier@email.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


from rest_framework.routers import DefaultRouter
from compras.views import (
    ProveedorViewSet,
    ProductoViewSet,
    OrdenCompraViewSet,
    DetalleOrdenViewSet
)


router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'ordenes', OrdenCompraViewSet)
router.register(r'detalles', DetalleOrdenViewSet)

from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensaje": "API Gestión de Compras funcionando"})

from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),
    
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


