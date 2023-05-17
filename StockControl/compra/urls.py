from django.urls import path
from . import views
"""Lista de endpoints con sus respectivas vistas e identificadores de referencia."""

urlpatterns = [
    path('productos/listado/', views.ProductoListView.as_view(), name="mostrar_productos"),
    path('productos/crear/', views.ProductoCreateView.as_view(), name="crear_producto"),
    path('proveedores/listado/', views.ProveedorListView.as_view(), name="mostrar_proveedores"),
    path('proveedores/crear/', views.ProveedorCreateView.as_view(), name="crear_proveedor")
]
