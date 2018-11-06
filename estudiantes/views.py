from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CursoForm, EstudianteForm
from estudiantes.models import Estudiante, Curso
from django.contrib import messages


def index(request):
    return render(request, 'estudiante/index.html')


def estudiante_list(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'estudiante/listar_estudiante.html', {'estudiante':estudiante})


def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'estudiante/listar_cursos.html', {'curso':curso})



def curso_nuevo(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            add=formulario.save(commit=False)
            add.save()
            formulario.save_m2m()
            return redirect('curso_list')
    else:

        formulario = CursoForm()

    return render(request, 'estudiante/curso_nuevo.html', {'formulario': formulario})


def estudiante_nuevo(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'estudiante/estudiante_nuevo.html', {'form': form})
