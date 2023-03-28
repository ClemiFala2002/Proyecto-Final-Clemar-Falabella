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
from OnlyTrucks.views import (index, CamionList, CamionDetail, CamionUpdate, CamionDelete, CamionCreate, CamionSearch, 
                              RemolqueList, RemolqueDetail, RemolqueUpdate, RemolqueDelete, RemolqueCreate, buscar_post, Login,
                              SignUp,Logout, CamionMyList, RemolqueMyList, ProfileCreate, ProfileUpdate,about, MensajeCreate, MensajeDelete, MensajeList)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', index, name="index"), 
   path('Camion/list', CamionList.as_view() , name="Camion-list"),
   path('Camion/<pk>/detail', CamionDetail.as_view() , name="Camion-detail"),
   path('Camion/<pk>/update', CamionUpdate.as_view() , name="Camion-update"),
   path('Camion/<pk>/delete', CamionDelete.as_view() , name="Camion-delete"),
   path('Camion/create', CamionCreate.as_view() , name="Camion-create"),
   path('Camion/search', CamionSearch.as_view() , name="Camion-search"),
   path('Acoplados/list', RemolqueList.as_view() , name="Remolques-list"),
   path('Acoplados/<pk>/detail', RemolqueDetail.as_view() , name="Remolques-detail"),
   path('Acoplados/<pk>/update', RemolqueUpdate.as_view() , name="Remolques-update"),
   path('Acoplados/<pk>/delete', RemolqueDelete.as_view() , name="Remolques-delete"),
   path('Acoplados/create', RemolqueCreate.as_view() , name="Remolques-create"),
   path('Camiones/buscar', buscar_post, name="buscar-camion"),
   path('Login/', Login.as_view() , name="login"),
   path('Signup/', SignUp.as_view() , name="signup"),
   path('Logout/', Logout.as_view() , name="logout"),
   path('Camion/list/My', CamionMyList.as_view() , name="camionmylist"),
   path('Acoplados/list/My', RemolqueMyList.as_view() , name="remolquemylist"),
   path('Profile/create', ProfileCreate.as_view() , name="Profile-create"),
   path('Profile/<pk>/update', ProfileUpdate.as_view() , name="Profile-update"),
   path('About/', about, name="about"), 
   path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
   path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create" ),
   path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
   
   
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
