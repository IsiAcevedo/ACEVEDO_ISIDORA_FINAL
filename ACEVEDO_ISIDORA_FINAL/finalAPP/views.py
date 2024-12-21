from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import redirect, render
from .forms import FormParticipante, FormInstitucion
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Vistas HTML
def index(request):
    return render(request, 'index.html')

def listado(request):
    participantes = Participante.objects.all()
    data = {'participantes': participantes}
    return render(request, 'listado.html', data)

def instituciones(request):
    instituciones = Institucion.objects.all()
    data = {'instituciones': instituciones}
    return render(request, 'instituciones.html', data)

def agregar_seminario(request):
    form = FormParticipante()

    if request.method == 'POST':
        form = FormParticipante(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listado/')
    
    data = {'formP': form}
    return render(request, 'agregar_participantes.html', data)

def agregar_institucion(request):
    form = FormInstitucion()

    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    
    data = {'form': form}
    return render(request, 'agregar_institucion.html', data)

def eliminar_seminario(request, id):
    participante = Participante.objects.get(id=id)
    participante.delete()
    messages.success(request, 'Participante eliminado exitosamente.')
    return redirect('/listado/')

def actualizar_seminario(request, id):
    participante = Participante.objects.get(id=id)
    form = FormParticipante(instance=participante)
    
    if request.method == 'POST':
        form = FormParticipante(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participante actualizado exitosamente.')
            return redirect('/listado/')
    
    data = {'formP': form}
    return render(request, 'agregar_participantes.html', data)

def eliminar_institu(request, id):
    instituciones = Institucion.objects.get(id=id)
    instituciones.delete()
    messages.success(request, 'Institución eliminada exitosamente.')
    return redirect('/')


# API REST para Seminarios 
class Seminarios(generics.ListCreateAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class SeminariosView_edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

# API REST para Instituciones
class Instituciones(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class InstituView_edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer


@api_view(['GET'])
def autor(request):
    autor = {
        "nombre": "Isidora",
        "apellido": "Acevedo",
        "email": "isidora.acevedo02@inacap.cl",
        "carrera": "Analista Programador",
        "ramo": "Programación Back End"
    }
    return Response(autor)