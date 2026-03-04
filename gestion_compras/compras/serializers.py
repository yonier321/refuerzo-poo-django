from rest_framework import serializers
from .models import Proveedor, Producto, OrdenCompra, DetalleOrden

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
    def validate(self, data):
        proveedor = data.get('proveedor')
        
        if not proveedor.estado:
            raise serializers.ValidationError(
                "No se puede crear producto con proveedor inactivo."
            )
        if data.get('precio') <= 0:
            raise serializers.ValidationError(
                "El precio debe ser mayor a 0"
            )
        return data

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'
        read_only_fields = ('subtotal',)
        
    def validate(self, data):
        if data.get('cantidad') <= 0:
            raise serializers.ValidationError(
                "la cantidad debe ser mayor a 0"
            )
        return data 
    
class OrdenCompraSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True, read_only=True)
    
    class Meta: 
        model= OrdenCompra
        fields = '__all__'
        read_only_fields = ('total',)
        
    def validate(self, data):
        proveedor = data.get('proveedor')
        
        if not proveedor.estado:
            raise serializers.ValidationError(
                "No se puede crear orden con el proveedor inactivo."
            )
        return data 

    def update(self, instance, validated_data):
        estado_anterior = instance.estado
        nuevo_estado = validated_data.get('estado', instance.estado)

        instance.estado = nuevo_estado
        instance.save()

        # Si se aprueba la orden
        if estado_anterior != 'aprobada' and nuevo_estado == 'aprobada':
            total = 0

            for detalle in instance.detalles.all():
                total += detalle.subtotal

                # Regla 5: actualizar stock
                producto = detalle.producto
                producto.stock += detalle.cantidad
                producto.save()

            instance.total = total
            instance.save()

        return instance
       
        
        
        
        
        
        
        
    
    
    

    
            
    