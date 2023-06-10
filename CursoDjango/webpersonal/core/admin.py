from django.contrib import admin
from .models import Asignatura, ClaseHorario, UsuarioExtendido, Aula

# Register your models here.
admin.site.register(Asignatura)
admin.site.register(ClaseHorario)
admin.site.register(UsuarioExtendido)
admin.site.register(Aula)
