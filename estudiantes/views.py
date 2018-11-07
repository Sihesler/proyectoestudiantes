from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CursoForm, EstudianteForm
from estudiantes.models import Estudiante, Curso
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'estudiante/index.html')

@login_required
def estudiante_detalle(request, pk):
        estudiante = get_object_or_404(Estudiante, pk=pk)
        return render(request, 'estudiante/estudiante_detalle.html', {'estudiante': estudiante})

@login_required
def curso_detalle(request, pk):
        curso = get_object_or_404(Curso, pk=pk)
        return render(request, 'estudiante/curso_detalle.html', {'curso': curso})


def estudiante_list(request):
    estudiante = Estudiante.objects.all()
    return render(request, 'estudiante/listar_estudiante.html', {'estudiante':estudiante})


def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'estudiante/listar_cursos.html', {'curso':curso})

@login_required
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

@login_required
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

@login_required
def estudiante_remove(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect('estudiante_list')

@login_required
def curso_remove(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('curso_list')

@login_required
def curso_editar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        formulario = CursoForm(request.POST,request.FILES, instance=curso)
        if formulario.is_valid():
            curso_edit=formulario.save(commit=False)
            formulario.save_m2m()
            curso_edit.save()
            return redirect('curso_detalle', pk=curso_edit.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'estudiante/curso_editar.html', {'form': form})

@login_required
def estudiante_editar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        formulario = EstudianteForm(request.POST, instance=estudiante)
        if formulario.is_valid():
            estudiante_edit = formulario.save(commit=False)
            estudiante_edit.save()
            return redirect('estudiante_detalle', pk=estudiante_edit.pk)
    else:
        form = EstudianteForm(instance=estudiante)
        return render(request, 'estudiante/estudiante_editar.html', {'form': form})
