from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado

def index(request):

    return render(request,'miapp/index.html')    

def comunicados(request):
    comunicados = Comunicado.objects.filter(visible=True)
    ultimos = Comunicado.objects.filter(visible=True)[:3]

    context = {
        'comunicados': comunicados,
        'ultimos': ultimos
    }

    return render(request,'miapp/comunicado.html', context=context)
