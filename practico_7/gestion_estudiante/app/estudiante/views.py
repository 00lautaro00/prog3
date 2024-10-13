from django.shortcuts import render
from .models import Estudiante, Curso

# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar_estudiantes(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'listar_estudiante.html', {'estudiante': estudiante})


def listar_por_parametro(request):
    edad = request.GET.get('edad')
    estudiante = Estudiante.objects.filter(edad__gt = edad)
    return render(request, 'listar_estudiante.html', {'estudiante': estudiante})

def listar_cursos(request):
    curso = Curso.objects.all()
    return render(request, 'listar_curso.html', {'curso': curso})

def findOneCurso(request, id):
    curso = Curso.objects.get( id = id)
    return render(request, 'curso.html', {'curso': curso})