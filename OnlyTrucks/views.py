from django.shortcuts import render
from OnlyTrucks.models import Post, Remolques, Concesionaria
from OnlyTrucks.forms import PostForm, RemolquesForm, ConsesionariaForm

def index(request):
    return render(request, "OnlyTrucks/index.html")

def Resultado_de_Busqueda(request):
    
    posts = Post.objects.all()
    return render(request, "OnlyTrucks/Resultado_de_Busqueda.html",{"posts": posts})

def mostrar_post(request):
    
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    
    return render(request, "OnlyTrucks/admin_post.html", context )

def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    
    return render(request, "OnlyTrucks/admin_post.html", context)

def buscar_post(request):
    criterio= request.GET.get("criterio")
    context = {
        "posts":Post.objects.filter(Modelo_de_su_Camion__icontains=criterio).all(),
    }
    
    return render(request, "OnlyTrucks/Camiones.html", context)


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
