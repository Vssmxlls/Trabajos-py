accion_votos = 0
ciencia_ficcion_votos = 0
pregunta = 15

for i in range (pregunta):
    print("Bienvenido al menu de seleccion de genero preferido de Netflix")
    print("1.Accion")
    print("2.Ciencia Ficcion")
    respuesta = int(input("Ingrese por favor el numero del genero de acuerdo al menu: "))
    if (respuesta == 1):
        accion_votos +=1
    elif (respuesta == 2):
        ciencia_ficcion_votos +=1
if (accion_votos > ciencia_ficcion_votos):
    # comment: 
    print("El genero mas votado fue el genero de accion")
elif (ciencia_ficcion_votos > accion_votos):
    print("El genero mas votado fue el genero de ciencia ficcion")


print("El genero de accion tuvo: ", accion_votos, "votos en total")
print("El genero de ciencia ficcion tuvo: ", ciencia_ficcion_votos, "votos en total")


    