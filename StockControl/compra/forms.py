from django import forms
from .models import Proveedor,Producto;

class ProveedoresForm(forms.ModelForm):
    """Crea un formulario a partir del modelo Proveedor."""
    class Meta:
        model = Proveedor
        fields = ["nombre","apellido","dni"]
        widgets = {
            "nombre" : forms.TextInput(attrs={"class":"form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.NumberInput(attrs={"class": "form-control"})
        }
class ProductoForm(forms.ModelForm):
    """Crea un formulario a partir del modelo Producto."""
    class Meta:
        model = Producto
        fields = ["nombre","precio","stock_actual","proveedor"]
        widgets = {
                    "nombre" : forms.TextInput(attrs={"class":"form-control"}),
                    "precio": forms.NumberInput(attrs={"class": "form-control"}),
                    "stock_actual": forms.NumberInput(attrs={"class": "form-control"}),
                    "proveedor": forms.Select(attrs={"class": "form-select"})
                }