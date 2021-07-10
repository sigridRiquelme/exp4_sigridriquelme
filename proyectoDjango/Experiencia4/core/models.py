from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class colaboradores(models.Model):
    rut = models.CharField(max_length = 12, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length = 80, verbose_name='Nombre')
    telefono = models.CharField(max_length = 9, verbose_name='Telefono')
    direccion = models.CharField(max_length = 100, verbose_name='Direccion')
    email = models.CharField(max_length = 200, verbose_name='Email')
    pais = models.CharField(max_length = 30, verbose_name='Pais')


    def str(self):

        return (self.rut)