from django.shortcuts import render
from .models import colaboradores

# Create your views here.

def index(request):

    return render(request, 'index.html')

def crud(request):

    Colaboradores = colaboradores.objects.all()

    return render(request, 'core/crud.html', context={'datos': Colaboradores})

