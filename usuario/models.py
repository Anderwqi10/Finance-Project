from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ROLE_CHOICES = (('Normal', 'normal'), ('Premiun', 'premiun'),)
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Normal')
    acepta_terminos = models.BooleanField(default=False)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.user.username

class Moneda(models.Model):
    id_moneda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    moneda = models.ForeignKey(to=Moneda, on_delete=models.CASCADE, null=True, blank=True, default=None)
    def __str__(self):
        return self.nombre

