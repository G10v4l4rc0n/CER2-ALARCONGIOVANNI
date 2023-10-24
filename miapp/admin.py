from django import forms
from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Entidad,Comunicado,User

class ModificadoPor(admin.ModelAdmin):
    readonly_fields = ('modificado_por','entidad', )
    
    
    def save_model(self, request, obj, form, change):
        obj.modificado_por = request.user
        obj.entidad = request.entidad
        super(ModificadoPor, self).save_model(request, obj, form, change)

admin.site.register(Entidad)
admin.site.register(Comunicado, ModificadoPor)
admin.site.register(User)