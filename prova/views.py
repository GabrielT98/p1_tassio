
from django.shortcuts import render
from prova.entity import Restaurante,Especialista

especialista1 = Especialista("GAbriel","melhor restaurante da cidade")
especialista2 =  Especialista("Lucas","Barato e bom")
especialista3 = Especialista("Thiago","Comida diretamento do Líbano")

restaurante1= Restaurante(1,"Varandas","Rua Jesus é o poder,Número 30, Centro, Vassouras","https://www.google.com/url?sa=i&url=https%3A%2F%2Frestaurantguru.com.br%2FRestaurante-Varandas-Vassouras&psig=AOvVaw3ANhYVS459sOA4el7_ZRmF&ust=1649457973222000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCNCh-YKEg_cCFQAAAAAdAAAAABAD",
                          "10:00 - 18:00",especialista1)

restaurante2 = Restaurante(2,"Sabor do Vale","Rua das Oliveiras,Número 40,Centro,VAssouras","https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.tripadvisor.com.br%2FLocationPhotoDirectLink-g1598517-d5362075-i312047573-Restaurante_Sabor_Do_Vale-Vassouras_State_of_Rio_de_Janeiro.html&psig=AOvVaw3DpzXOZYCHdVkkZoCHUPDc&ust=1649458155783000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCMC4lNCEg_cCFQAAAAAdAAAAABAD",
                           "12:00 - 20:00",especialista2)


restaurantes = [restaurante1,restaurante2]

def listar_restaurantes(request):
    return render(request,"index.html",{"restaurantes":restaurantes})

def ver_restaurante(request,id:int):
    for restaurante in restaurantes:
        if restaurante.get_id() == id:
            return render(request, "restaurante.html", {"restaurante": restaurante})
