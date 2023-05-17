from django.db import models

# Create your models here.
class Proveedor(models.Model):
    """Crea un modelo de la entidad Proveedor."""

    nombre = models.CharField(max_length=50,default="");
    apellido = models.CharField(max_length=50,default="");
    dni = models.IntegerField(default=0);
    
    def __str__(self):
        """Retorna una cadena con los campos nombre y apellido del modelo Proveedor"""

        return f'{self.nombre} {self.apellido}';


class Producto(models.Model):
    """Crea un modelo de la entidad Producto."""

    nombre = models.CharField(max_length=50, default="")
    precio = models.FloatField(default=0)
    stock_actual = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="proveedor")

    def __str__(self):
        """Retorna una cadena con los campos del modelo Producto"""

        return f'Nombre : {self.nombre} \n Precio: {self.precio} \n Stock: {self.stock_actual} \n Proveedor: {self.proveedor}'
