from django.db import models
from ckeditor.fields import RichTextField

class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name="Matricula")#Texto corto
    nombre = models.TextField() #Texto Largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    edad = models.IntegerField()
    imagen = models.ImageField(null=True,upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Crear") #Fecha y tiempo
    update = models.DateTimeField(auto_now_add=True, verbose_name="Actualizar")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering =["-created"]
        #el menos indica que se ordenara del mas reciente al mas viejo

    def __str__(self):
             return self.nombre
     #Indica que se mostrara el nombre como valor en la tabla

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos,on_delete = models.CASCADE,verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")
    
    class Meta:
         verbose_name = "Comentario"
         verbose_name_plural = "Comentarios"
         ordering = ["-created"]
    
    def __str__(self):
        return self.coment
    
class ComentarioContacto(models.Model):
     id= models.AutoField(primary_key=True,verbose_name="Clave")
     usuario= models.TextField(verbose_name="Usuario")
     mensaje= models.TextField(verbose_name="Comentario")
     created= models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
     
     class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural="Comentarios Contactos"
        ordering=["-created"]
    
     def __str__(self):
        return self.mensaje
    #Indica que se mostrara el mensaje como valor en la tabla
    