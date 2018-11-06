from django.db import models
from django.contrib import admin

# Create your models here.
class Estudiante(models.Model):

    nombre           =  models.CharField(max_length=50)
    edad             =  models.IntegerField()
    fecha_nacimiento =  models.DateField()
    direccion        =  models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#////////////
class Curso(models.Model):

    materia     = models.CharField(max_length=60)
    profesor    = models.CharField(max_length=60)
    hora        = models.CharField(max_length=20)
    estudiantes = models.ManyToManyField(Estudiante, null=True, blank=True)

    def __str__(self):
        return self.materia
