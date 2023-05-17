from django.contrib import admin
from .models import Producto,Proveedor
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Registra el modelo Producto en el admin """

    list_display = ["id","nombre","precio","stock_actual","proveedor"]

@admin.register(Proveedor)

class ProveedorAdmin(admin.ModelAdmin):
    """Registra el modelo Proveedor en el admin """

    list_display = ["id", "nombre", "apellido", "dni"]

