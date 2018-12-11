from django.contrib import admin

# Register your models here.
from registro.models import Pais, Evento

admin.site.register(Pais)
admin.site.register(Evento)

