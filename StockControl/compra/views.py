from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,DeleteView;
from django.views.generic.list import ListView;
from .models import Producto,Proveedor
from django.urls import reverse;
from . import forms

# Create your views here.

class ProveedorCreateView(CreateView):
    
    form_class = forms.ProveedoresForm
    template_name = 'compra/cargar_proveedor.html';

    def get_success_url(self):
        return reverse('compra:mostrar_proveedores');

class ProveedorListView(ListView):
    
    model = Proveedor;
    template_name = 'compra/mostrar_proveedores.html';
    context_object_name = 'proveedores';
    
    """ def get_context_data(self, **kwargs: Any):
        print(super().get_context_data(**kwargs)); """
        

class ProductoCreateView(CreateView):
    
    form_class = forms.ProductoForm;
    template_name = 'compra/cargar_producto.html';
    
    def get_success_url(self):
        return reverse('compra:mostrar_productos')

class ProductoListView(ListView):

    model = Producto;
    template_name = "compra/mostrar_productos.html"
    context_object_name = "productos";



def test(request):
    return HttpResponse("Hola");