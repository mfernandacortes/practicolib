from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("nuevo-autor", views.nuevo_autor, name='nuevo-autor'),
    path("autores", views.autores, name='autores'),
    path("clientes", views.clientes, name='clientes'),
    path("localidades", views.localidades, name='localidades'),
    path("ingresoPelicula", views.ingresoPelicula, name='ingresoPelicula')

]