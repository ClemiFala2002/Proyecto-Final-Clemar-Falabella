from django.db import models

class Post(models.Model):
    Modelo_de_su_Camion = models.CharField(max_length=30)
    Marca_de_su_Camion = models.CharField(max_length=80)
    Año_de_Fabricacion = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=120)
    Precio= models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.id} - {self.Modelo_de_su_Camion} - {self.Año_de_Fabricacion} - {self.Precio}"
    
class Remolques(models.Model):
    Modelo_de_su_Acoplado = models.CharField(max_length=30)
    Marca_de_su_Acoplado = models.CharField(max_length=80)
    Año_de_Fabricacion = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=120)
    Precio= models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.id} - {self.Modelo_de_su_Acoplado} - {self.Año_de_Fabricacion} - {self.Precio}"   
    
class Concesionaria(models.Model):
    Nombre_del_Consesionario = models.CharField(max_length=30)
    Direccion_del_Consesionario = models.CharField(max_length=80)
    Horarios_de_Atencion = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.id} - {self.Nombre_del_Consesionario} - {self.Direccion_del_Consesionario} - {self.Horarios_de_Atencion}"              