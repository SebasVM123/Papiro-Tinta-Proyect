from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class cliente(AbstractUser):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)

    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    fecha_registro = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name='clientes')
    user_permissions = models.ManyToManyField(Permission, related_name='clientes_permissions')

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class tarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=50)
    codigo = models.IntegerField()
    fecha_expiracion = models.DateField()

    banco = models.CharField(max_length=50)
    franquicia = models.CharField(max_length=50)

    propietario = models.CharField(max_length=200)


class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class cliente_tarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    id_tarjeta = models.ForeignKey(tarjeta, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)


class cliente_categoria(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
