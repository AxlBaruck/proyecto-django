from django.shortcuts import render
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
import datetime
#Accedemos al modelo Alumnos que contiene la estructura de la tabla


# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
#all recupera todos los objetos del modelo (registros de la tabla alumnos)

    return render(request, "registros/principal.html", {'alumnos':alumnos})
#Indicamos el lugar donde se renderizara el resultado de vista y enviamos

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvia al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form':form})

def contacto(request):
    return render(request,"registros/contacto.html")
#indicamos el lugar donde se renderizara el resultado de la vista

def comentarios(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request,"registros/comentario.html", {'comentarios':comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/comentario.html",{'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):

    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/formEditarComentario.html",

    {'comentario':comentario})


def editarComentarioContacto(request, id):

    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html", {'comentarios':comentarios})

    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"registros/formEditarComentario.html", {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.


def consultar1(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    #Si solo deseamos recuperar ciertos datos agregamos la
    #funcion only, listando los campos que queremos obtener de
    #la consulta emplear filter() o en el ejemplo all()
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2022,7,1)
    fechaFin = datetime.date(2022,7,13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    #Consultando modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No inscrito")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})