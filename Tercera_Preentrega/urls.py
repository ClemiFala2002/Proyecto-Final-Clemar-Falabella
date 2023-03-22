"""Tercera_Preentrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OnlyTrucks.views import index, mostrar_post, agregar_post, buscar_post, Resultado_de_Busqueda, mostrar_Remolque, agregar_Remolque, mostrar_Consesionaria, agregar_Consesionaria, Resultado_de_Remolque,Resultado_de_Consesionaria 

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', index, name="index"), 
   path('Resultado de Busqueda/', Resultado_de_Busqueda, name="Resultado Busqueda"), 
   path('Camiones/', mostrar_post, name="Busqueda"), 
   path('Camiones/agregar', agregar_post, name="agregar-camion"),
   path('Camiones/buscar', buscar_post, name="buscar-camion"),
   path('Acoplados/', mostrar_Remolque, name="Remolque"),
   path('Acoplados/agregar', agregar_Remolque, name="Agregar-Remolque"),
   path('Concesionario/', mostrar_Consesionaria, name="Consesionaria1"),
   path('Concesionario/agregar', agregar_Consesionaria, name="Agregar-Consesionaria"),
   path('Resultado de BusquedaR/', Resultado_de_Remolque, name="Resultado BusquedaR"), 
   path('Resultado de BusquedaC/', Resultado_de_Consesionaria, name="Resultado BusquedaC"),
]
