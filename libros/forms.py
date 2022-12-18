from django import forms

class AutorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=120)
    apellido = forms.CharField(label="Apellido", max_length=120)

class PeliForm(forms.Form):
    nombre = forms.CharField(label="Ingrese pelicula", max_length=100)
    fechaEst=forms.DateField(label="Fecha de estreno", 
                                    widget=forms.DateInput(attrs={"type":"date"}))
    mayoresDe = forms.IntegerField(label="Para mayores de")
    online = forms.BooleanField(label="Es preventa online?", required=False)

class principalForm(forms.Form):
    #Practico = forms.CharField(label="Seleccione el práctico")
    CHOICES = (('Practica 1', 'Practica 1'),('Practica 2', 'Practica 2'),)
    field = forms.ChoiceField(choices=CHOICES)