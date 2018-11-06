from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CursoForm, EstudianteForm
from estudiantes.models import Estudiante, Curso
from django.contrib import messages


def index(request):
    return render(request, 'estudiante/index.html')
