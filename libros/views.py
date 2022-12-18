from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
import sqlite3
from .forms import AutorForm, PeliForm
from .models import Persona, Localidad

# Create your views here.

def index(request, template_name="libros/index.html"):
    dato = {"saludo": "Bienvenido/a, esta es la app de prácticas de M.Fernanda Cortés"}
    return render(request, template_name, dato)


def autores(request, template_name="libros/autores.html"):
    conn = sqlite3.connect("contabilidad.sqlite")
    autor = conn.cursor()
    autor.execute("select nombre, apellido from autor")
    autor_list = autor.fetchall()
    dato = {"autor": autor_list}
    conn.close()
    return render(request, template_name, dato)

def nuevo_autor(request, template_name="libros/autor_form.html"):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            conn = sqlite3.connect('contabilidad.sqlite')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO autor VALUES (?, ?)",
                           (form.cleaned_data['nombre'], form.cleaned_data['apellido']))
            conn.commit()
            conn.close()
            return redirect('autores')
    else:
        form = AutorForm()
    dato = {"form": form }
    return render(request, template_name, dato)

def ingresoPelicula(request, template_name="libros/peli_form.html"):
    if request.method=="POST":
        form = PeliForm(request.POST)
        if form.is_valid():
            dato = {"form": form.cleaned_data}
            template_name = "libros/ejerciciopeli.html"
            return render(request, template_name, dato)
    else :
        form = PeliForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def clientes(request, template_name="libros/clientes.html"):
    cliente_list = Persona.objects.all()
    dato = {"clientes": cliente_list}
    return render(request, template_name, dato)

def localidades(request, template_name="libros/localidades.html"):
    localidad_list = Localidad.objects.all()
    dato = {"localidades": localidad_list}
    return render(request, template_name, dato)
