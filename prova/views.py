
from django.shortcuts import render
restaurantes = []

def listar_restaurantes(request):
    return render(request,"index.html",{"lista":restaurantes})

def ver_restaurante(request,id:int):
    pass