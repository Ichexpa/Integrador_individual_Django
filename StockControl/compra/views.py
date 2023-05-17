from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic.list import ListView
from .models import Producto,Proveedor
from django.urls import reverse
from . import forms

# Create your views here.

class ProveedorCreateView(CreateView):
    """Vista basada en clase ProveedorCreateView que hereda de CreateView, crea un nuevo 
       modelo y lo registra a partir de un formulario"""
    
    form_class = forms.ProveedoresForm
    template_name = 'compra/cargar_proveedor.html'


    def get_success_url(self):
        """Redirecciona a la vista mostrar_proveedores una vez que el modelo 
            se registro en la base de datos"""
        
        return reverse('compra:mostrar_proveedores')

class ProveedorListView(ListView):
    """Vista basada en clase ProveedorListView que hereda de ListView, captura los 
    registros en la base de datos de acuerdo al modelo indicado y lo envia por el contexto"""

    model = Proveedor
    template_name = 'compra/mostrar_proveedores.html'
    context_object_name = 'proveedores'
        

class ProductoCreateView(CreateView):
    """Vista basada en clase ProductoCreateView que hereda de CreateView, crea un nuevo 
       modelo y lo registra a partir de un formulario"""
    
    form_class = forms.ProductoForm
    template_name = 'compra/cargar_producto.html'
    
    def get_success_url(self):
        """Redirecciona a la vista mostrar_productos una vez que el modelo 
            se registro en la base de datos"""
        
        return reverse('compra:mostrar_productos')

class ProductoListView(ListView):
    """Vista basada en clase ProductoListView que hereda de ListView, captura los 
    registros en la base de datos de acuerdo al modelo indicado y lo envia por el contexto"""

    model = Producto
    template_name = "compra/mostrar_productos.html"
    context_object_name = "productos"