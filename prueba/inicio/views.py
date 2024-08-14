from django.shortcuts import render, HttpResponse

# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")

def contacto(request):

    return render(request,"inicio/contacto.html")

def formulario(request):
   
    return render(request,"inicio/formulario.html")

def ejemplo(request):
    return render(request,"inicio/ejemplo.html")

def seguridad(request):
    return render(request,"inicio/seguridad.html")

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"inicio/seguridad.html", {'nombre':nombre})


