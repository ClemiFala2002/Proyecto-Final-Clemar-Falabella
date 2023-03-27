from django.db import models
from django.contrib.auth.models import User

class Camion(models.Model):
    Modelo_de_su_Camion = models.CharField(max_length=30)
    Marca_de_su_Camion = models.CharField(max_length=80)
    Año_de_Fabricacion = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=120)
    Precio= models.CharField(max_length=10)
    Vendedor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Vendedor")
    
    def __str__(self):
        return f"{self.id} - {self.Modelo_de_su_Camion} - {self.Año_de_Fabricacion} - {self.Precio}"
    
class Remolques(models.Model):
    Modelo_de_su_Acoplado = models.CharField(max_length=30)
    Marca_de_su_Acoplado = models.CharField(max_length=80)
    Año_de_Fabricacion = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=120)
    Precio= models.CharField(max_length=10)
    Vendedor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vendedor")
    
    def __str__(self):
        return f"{self.id} - {self.Modelo_de_su_Acoplado} - {self.Año_de_Fabricacion} - {self.Precio}"   
    
          