from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono_personal = models.IntegerField(blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    TIPO_USUARIO = {
        'arrendatario':'arrendatario',
        'arrendador':'arrendador'
    }
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO, blank=True)

    def __str__(self) -> str:
        return f'{self.rut} {self.nombre}'
    

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre_comuna} - {self.region}'


class Inmueble(models.Model):
    propietario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    m2_construidos = models.FloatField()   
    m2_totales = models.FloatField()      
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING)
    TIPO_INMUEBLE = {
        'casa':'casa',
        'departamento':'departamento',
        'parcela':'parcela'
    }
    tipo_inmueble = models.CharField(choices=TIPO_INMUEBLE, max_length=20)
    precio_arriendo = models.IntegerField()
    disponible = models.BooleanField(default=True)
    solicitudes = models.JSONField(blank=True, null=True)
    arrendatario = models.OneToOneField(Usuario, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='arrendatario')

    def __str__(self) -> str:
        return f'{self.nombre} propietario: {self.propietario} arrendatario: {self.arrendatario}'