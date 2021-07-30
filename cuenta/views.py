from django.http import HttpResponse
from django.template import Template, Context
#from django.template import loader
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    return HttpResponse("Hola Mundo")

def saludo2(request):
    p1=Persona("Leonardo","Chacon")
    dic={"nombre":p1.nombre, "apellido":p1.apellido}
    return render(request, "miplantilla.html", dic)

def hija1(request):
    return render(request,"hija1.html")

def hija2(request):
    return render(request,"hija2.html")
