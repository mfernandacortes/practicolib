from django.db import models
import sqlite3

# Create your models here.

TIPO_IVA_CHOICE = (
    ("CF", "Consumidor Final"),
    ("RI", "Responsable Inscripto"),
    ("MT", "Monotributo")
)

class Autor(models.Model):
    nombre = models.CharField("Nombre Autor", max_length=50)
    apellido = models.CharField("Apellido Autor", max_length=50)


class Libro(models.Model):
    titulo = models.CharField("titulo.Libro", max_length=50)
    editorial = models.CharField("autor.Libro", max_length=50)
    autor = models.ForeignKey(Autor, on_delete= models.PROTECT, null=True, blank=True)

class Localidad(models.Model):
    nombre = models.CharField("Nombre Localidad", max_length=150)
    cp = models.CharField("Codigo Postal", max_length=10)
    provincia = models.CharField(max_length=50)

class Persona(models.Model):
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=150)
    edad = models.IntegerField(null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fecha_nac=models.DateField("Fecha de nacimiento", null=True, blank=True)
    tipo_iva = models.CharField("Tipo de IVA", max_length=2, choices=TIPO_IVA_CHOICE, default="CF")