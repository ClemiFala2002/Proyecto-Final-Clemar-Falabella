from django.db import models
from django.contrib.auth.models import User

class Camion(models.Model):
    Modelo_de_su_Camion = models.CharField(max_length=30)
    Marca_de_su_Camion = models.CharField(max_length=80)
    Año_de_Fabricacion = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=120)
    Precio= models.CharField(max_length=10)
    Vendedor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Vendedor")
    Imagen= models.ImageField(upload_to="camiones", null=True, blank=True)
    Publicado_el = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_url(self):
        return self.Imagen.url if self.Imagen else ''
        
   
    def __str__(self):
        return f"{self.id} - {self.Modelo_de_su_Camion} - {self.Año_de_Fabricacion} - {self.Precio}"
    

class Remolques(models.Model):
    Modelo_de_su_Acoplado = models.CharField(max_length=30)
    Marca_de_su_Acoplado = models.CharField(max_length=80)
    Año_de_Fabricacion = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=120)
    Precio= models.CharField(max_length=10)
    Vendedor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="vendedor")
    Imagen= models.ImageField(upload_to="remolques", null=True, blank=True)
    Publicado_el = models.DateTimeField(auto_now_add=True)
    
    @property
    def imagen_url(self):
        return self.Imagen.url if self.Imagen else ''
    
   
    def __str__(self):
        return f"{self.id} - {self.Modelo_de_su_Acoplado} - {self.Año_de_Fabricacion} - {self.Precio}"   
    
    
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile") 
    Facebook = models.CharField(max_length=150)
    Instagram = models.CharField(max_length=150)
    Twitter = models.CharField(max_length=150)
    avatar= models.ImageField(upload_to="avatares", null=True, blank=True)  
    
    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''
   
    
    
    
class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")     
    
          