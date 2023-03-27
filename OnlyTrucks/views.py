from django.shortcuts import render
from OnlyTrucks.models import Camion, Remolques, Profile
from OnlyTrucks.forms import CamionForm, RemolquesForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "OnlyTrucks/index.html")

class CamionList(ListView):
    model = Camion
    context_object_name = "Camiones"
    
class CamionDetail(DetailView):
    model = Camion 
    context_object_name = "Camion"   
    
class CamionUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Camion 
    success_url = reverse_lazy("Camion-list")
    fields = '__all__' 
    
    def test_func(self):
       user_id= self.request.user.id 
       camion_id= self.kwargs.get("pk")
       return Camion.objects.filter(Vendedor=user_id, id= camion_id).exists() 
        
    
class CamionDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Camion
    success_url = reverse_lazy("Camion-list")
    
    def test_func(self):
       user_id= self.request.user.id 
       camion_id= self.kwargs.get("pk")
       return Camion.objects.filter(Vendedor=user_id, id= camion_id).exists() 
    
class CamionCreate(LoginRequiredMixin,CreateView):
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
    
class RemolqueUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Remolques
    success_url = reverse_lazy("Remolques-list")
    fields = '__all__' 
    
    def test_func(self):
       user_id= self.request.user.id 
       remolque_id= self.kwargs.get("pk")
       return Remolques.objects.filter(Vendedor=user_id, id= remolque_id).exists() 
    
class RemolqueDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Remolques
    success_url = reverse_lazy("Remolques-list")
    
    def test_func(self):
       user_id= self.request.user.id 
       remolque_id= self.kwargs.get("pk")
       return Remolques.objects.filter(Vendedor=user_id, id= remolque_id).exists()  
    
class RemolqueCreate(LoginRequiredMixin,CreateView):
    model = Remolques    
    success_url = reverse_lazy("Remolques-list") 
    fields = '__all__'    
    
def buscar_post(request):
    criterio= request.GET.get("criterio")
    context = {
        "CamionesB":Camion.objects.filter(Modelo_de_su_Camion__icontains=criterio).all(),
        "RemolquesB":Remolques.objects.filter(Modelo_de_su_Acoplado__icontains=criterio).all(),
        
    }
    
    return render(request, "OnlyTrucks/Resultado_de_Busqueda.html", context) 

class Login(LoginView):
    next_page = reverse_lazy("index") 
    
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')    
    
class Logout(LogoutView):
    template_name = "registration/logout.html"     
    
       
class CamionMyList(LoginRequiredMixin,CamionList):
    def get_queryset(self):
        return Camion.objects.filter(Vendedor=self.request.user.id).all()
    
class RemolqueMyList(LoginRequiredMixin,RemolqueList):
    def get_queryset(self):
        return Remolques.objects.filter(Vendedor=self.request.user.id).all()  
    
    
class ProfileCreate(CreateView):
    model = Profile  
    success_url = reverse_lazy('index') 
    fields = {'avatar','Facebook','Instagram','Twitter'}   
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
        
class ProfileUpdate(UserPassesTestMixin,UpdateView):
    model = Profile
    success_url = reverse_lazy('index')
    fields = {'avatar','Facebook','Instagram','Twitter'}
    
    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
    
    
            