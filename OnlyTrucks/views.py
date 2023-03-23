from django.shortcuts import render
from OnlyTrucks.models import Camion, Remolques, Concesionaria
from OnlyTrucks.forms import CamionForm, RemolquesForm, ConsesionariaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "OnlyTrucks/index.html")

def Resultado_de_Camion(request):
    
    Camiones = Camion.objects.all()
    return render(request, "OnlyTrucks/Resultado_de_Busqueda.html",{"Camiones": Camiones})

def mostrar_Camion(request):
    
    context = {
        "form": CamionForm(),
        "Camiones": Camion.objects.all(),
    }
    
    return render(request, "OnlyTrucks/Camiones.html", context )

def agregar_Camion(request):
    post_form = CamionForm(request.POST)
    post_form.save()
    context = {
        "form": CamionForm(),
        "Camiones": Camion.objects.all(),
    }
    
    return render(request, "OnlyTrucks/Camiones.html", context)

def buscar_Camion(request):
    criterio= request.GET.get("criterio")
    context = {
        "Camiones":Camion.objects.filter(Modelo_de_su_Camion__icontains=criterio).all(),
    }
    
    return render(request, "OnlyTrucks/Resultado_de_Busqueda.html", context)


def Resultado_de_Remolque(request):
    
    remolques = Remolques.objects.all()
    return render(request, "OnlyTrucks/Resultado_de_Busqueda_R.html",{"Remolques": remolques})

def mostrar_Remolque(request):
    
    context = {
        "formr": RemolquesForm(),
        "Remolques": Remolques.objects.all(),
    }
    
    return render(request, "OnlyTrucks/Remolques.html", context )

def agregar_Remolque(request):
    remolques_form = RemolquesForm(request.POST)
    remolques_form.save()
    context = {
        "formr": RemolquesForm(),
        "Remolques": Remolques.objects.all(),
    }
    return render(request, "OnlyTrucks/Remolques.html", context)

def Resultado_de_Consesionaria(request):
    
    concesionaria = Concesionaria.objects.all()
    return render(request, "OnlyTrucks/Resultado_de_Busqueda_C.html",{"concesionaria": concesionaria})

def mostrar_Consesionaria(request):
    
    context = {
        "formc": ConsesionariaForm(),
        "Consesionaria": Concesionaria.objects.all(),
    }
    
    return render(request, "OnlyTrucks/Consesionaria.html", context )

def agregar_Consesionaria(request):
    remolques_form = ConsesionariaForm(request.POST)
    remolques_form.save()
    context = {
        "formc": ConsesionariaForm(),
        "Consesionaria": Concesionaria.objects.all(),
    }
    return render(request, "OnlyTrucks/Consesionaria.html", context)

class CamionList(ListView):
    model = Camion
    context_object_name = "Camiones"
    
class CamionDetail(DetailView):
    model = Camion 
    context_object_name = "Camion"   
    
class CamionUpdate(UpdateView):
    model = Camion 
    success_url = reverse_lazy("Camion-list")
    fields = '__all__' 
    
class CamionDelete(DeleteView):
    model = Camion
    success_url = reverse_lazy("Camion-list")
    
class CamionCreate(CreateView):
    model = Camion    
    success_url = reverse_lazy("Camion-list") 
    fields = '__all__'
    
class CamionSearch(ListView):
    model = Camion
    context_object_name = "Camiones"
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result= Camion.objects.filter(Modelo_de_su_Camion__icontains=criterio).all()
        return result   
    
