from django.db import models

# Create your models here.

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    zona_horaria = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)



