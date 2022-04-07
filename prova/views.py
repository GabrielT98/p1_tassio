
from django.shortcuts import render
from prova.entity import Restaurante,Especialista

especialista1 = Especialista("Gabriel","melhor restaurante da cidade")
especialista2 =  Especialista("Lucas","Barato e bom")
especialista3 = Especialista("Thiago","Comida diretamento do Líbano")

restaurante1= Restaurante(1,"Varandas","Rua Jesus é o poder,Número 30, Centro, Vassouras","https://brasillocais.com/photo/106051.jpg",
                          "10:00 - 18:00",[especialista1,especialista3])

restaurante2 = Restaurante(2,"Sabor do Vale","Rua das Oliveiras,Número 40,Centro,Vassouras","https://media-cdn.tripadvisor.com/media/photo-s/12/99/81/69/fachada.jpg",
                           "12:00 - 20:00",[especialista2])


restaurantes = [restaurante1,restaurante2]

def listar_restaurantes(request):
    return render(request,"index.html",{"restaurantes":restaurantes})

def ver_restaurante(request,id:int):
    for restaurante in restaurantes:
        if restaurante.get_id() == id:
            return render(request, "restaurante.html", {"restaurante": restaurante})
