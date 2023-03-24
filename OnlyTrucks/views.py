from django.shortcuts import render
from OnlyTrucks.models import Camion, Remolques
from OnlyTrucks.forms import CamionForm, RemolquesForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "OnlyTrucks/index.html")

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

    
class RemolqueList(ListView):
    model = Remolques
    context_object_name = "Remolques"  
    
class RemolqueDetail(DetailView):
    model = Remolques 
    context_object_name = "Remolque"      
    
class RemolqueUpdate(UpdateView):
    model = Remolques
    success_url = reverse_lazy("Remolques-list")
    fields = '__all__' 
    
class RemolqueDelete(DeleteView):
    model = Remolques
    success_url = reverse_lazy("Remolques-list")
    
class RemolqueCreate(CreateView):
    model = Remolques    
    success_url = reverse_lazy("Remolques-list") 
    fields = '__all__'    