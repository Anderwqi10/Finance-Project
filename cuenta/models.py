from django.db import models
from usuario.models import Usuario, Pais, Moneda

# Create your models here.
class Banco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class BancoPais(models.Model):
    id = models.AutoField(primary_key=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, related_name="paises")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="bancos")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.banco.nombre} - {self.pais.nombre}"


class Cuenta(models.Model):
    TIPO_CHOICES = [
        ("Ahorro", "Ahorro"),
        ("Corriente", "Corriente"),
    ]

    id_cuenta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuentas")
    banco = models.ForeignKey(Banco, on_delete=models.SET_NULL, null=True, blank=True, related_name="cuentas")
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)  # Solo Ahorro o Corriente
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Automática
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name="cuentas")
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cuenta {self.id_cuenta} - Usuario {self.usuario.user.username}"


class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name="tarjetas")
    banco = models.ForeignKey(Banco, on_delete=models.SET_NULL, null=True, blank=True, related_name="tarjetas")
    numero = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50)  # Visa, MasterCard, etc.
    fecha_expiracion = models.DateField()
    limite_credito = models.DecimalField(max_digits=12, decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tarjeta {self.numero} - {self.marca}"
