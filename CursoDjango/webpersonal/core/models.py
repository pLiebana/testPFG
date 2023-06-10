from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

"""class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)"""


class Asignatura(models.Model):
    nombreAsignatura = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreAsignatura


class UsuarioExtendido(models.Model):
    # Los tipos de usuario posibles
    ADMIN = 1
    PROFESOR = 2
    ALUMNO = 3

    TIPOS_USUARIO = [
        (ADMIN, 'Admin'),
        (PROFESOR, 'Profesor'),
        (ALUMNO, 'Alumno'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.IntegerField(choices=TIPOS_USUARIO, default=ALUMNO)

    @property
    def es_admin(self):
        """Comprueba si el usuario es administrador."""
        return self.tipo_usuario == self.ADMIN

    @property
    def es_profesor(self):
        """Comprueba si el usuario es profesor."""
        return self.tipo_usuario == self.PROFESOR

    @property
    def es_alumno(self):
        """Comprueba si el usuario es alumno."""
        return self.tipo_usuario == self.ALUMNO

    def __str__(self):
        """String para representar el objeto UsuarioExtendido"""
        return self.user.username  # Devuelve el nombre de usuario


@receiver(post_save, sender=User)
def create_usuario_extendido(sender, instance, created, **kwargs):
    if created:
        UsuarioExtendido.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_usuario_extendido(sender, instance, **kwargs):
    instance.usuarioextendido.save()


class Aula(models.Model):
    # Campo para el nombre del aula
    nombre = models.CharField(max_length=100)

    # Campo para el edificio donde está el aula
    edificio = models.CharField(max_length=100)

    def __str__(self):
        """String para representar el objeto Aula"""
        return f'{self.nombre} - {self.edificio}'


class ClaseHorario(models.Model):
    DIAS_DE_LA_SEMANA = [
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
    ]
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor = models.ForeignKey(
        UsuarioExtendido,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo_usuario': UsuarioExtendido.PROFESOR},
        null=True,
    )
    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True, blank=True)  # Campo aula relacionado con el modelo Aula
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    diaSemana = models.IntegerField(choices=DIAS_DE_LA_SEMANA)
