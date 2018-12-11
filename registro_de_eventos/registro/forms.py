from django import forms
from .models import Pais

class pais_form(forms.Form):
    nombre = forms.CharField(label='Nombre del Pais', max_length=200)
    zona_horaria = forms.IntegerField(label='Zona horaria')

class evento_form(forms.Form):
    nombre = forms.CharField(label='Nombre del Evento', max_length=200)
    fecha = forms.DateTimeField()
    pais = forms.ModelChoiceField(queryset=Pais.objects.all())