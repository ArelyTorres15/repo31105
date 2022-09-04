from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

def curso(request):
    curso=Curso(nombre="ingles", comision=369)
    curso2=Curso(nombre="espeleologia", comision=147)
    curso3=Curso(nombre="programacion", comision=258)
    curso.save()
    curso2.save()
    curso3.save()
    texto=f"Curso Creados"
    return HttpResponse(texto)