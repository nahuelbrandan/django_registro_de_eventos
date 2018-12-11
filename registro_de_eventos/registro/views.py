import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Evento, Pais
from .forms import pais_form, evento_form

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home_view(request):
    eventos = Evento.objects.all()
    return render(request, 'home.html', {'eventos': eventos})


@require_http_methods(["GET", "POST"])
def pais_view(request):
    if request.method == 'GET':
        form = pais_form()
    else:
        # create a form instance and populate it with data from the request:
        form = pais_form(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Pais(**form.cleaned_data)
            obj.save()
            # redirect to a new URL:
            return HttpResponse('PAIS AGREGADO CON EXITO/')

    return render(request, 'pais.html', {'form':form})


@require_http_methods(["GET", "POST"])
def evento_view(request):
    if request.method == 'GET':
        form = evento_form()
    else:
        # create a form instance and populate it with data from the request:
        form = evento_form(request.POST)
        if form.is_valid():
            obj = Evento(**form.cleaned_data)
            obj.save()
            return HttpResponse('EVENTO AGREGADO CON EXITO/')

    return render(request, 'evento.html', {'form': form})