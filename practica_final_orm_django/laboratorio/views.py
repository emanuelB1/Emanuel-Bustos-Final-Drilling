from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import LaboratorioForm
from .models import Laboratorio

# Create your views here.

def mostrar(request):
    laboratorios = models.Laboratorio.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'laboratorios':laboratorios,
        'num_visits': num_visits,
    }
    return render(request,'mostrar.html', context)
    


def insertar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
        
    else:
        form = LaboratorioForm()
    
    return render(request, 'insertar.html', {'form': form})


def editar(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editar.html', {'form': form})


def eliminar(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/')  # Reemplaza 'nombre_de_la_vista' con el nombre de la vista a la que deseas redirigir después de eliminar el laboratorio

    return render(request, 'eliminar.html', {'laboratorio': laboratorio})