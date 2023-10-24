from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField()

    def __str__(self) -> str:
        return self.nombre
    
class User(AbstractUser):
    entidadPerteneciente = models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, blank=True)

class Comunicado(models.Model):
    Tipo_Choices = [
        ("S","suspensión de actividades"),
        ("C","suspensión de clases"),
        ("I","información")
    ]

    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=200)
    detalle_corto = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30,choices=Tipo_Choices,default="I")
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.titulo