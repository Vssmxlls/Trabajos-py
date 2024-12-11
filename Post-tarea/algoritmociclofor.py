personas = 10
estrella_1 = 0
estrella_2 = 0
estrella_3 = 0
estrella_4 = 0
estrella_5 = 0
for i in range (personas):
    # comment: 
    print("Bienvenido al menu de experiencia")
    print("A.1 Estrella")
    print("B.2 Estrella")
    print("C.3 Estrella")
    print("D.4 Estrella")
    print("E.5 Estrella")
    
    eleccion = input("Ingrese por favor la letra acorde a su satisfaccionj con la compra hecha: ")
    if (eleccion == "A"):
        estrella_1 +=1
        # comment: 
    # end if
    elif (eleccion == "B"):
        # comment: 
        estrella_2 +=1
    elif (eleccion == "C"):
        # comment: 
        estrella_3 +=1
    elif (eleccion == "D"):
        # comment: 
        estrella_4 +=1
    elif (eleccion == "E"):
        # comment: 
        estrella_5 +=1
# end for

print("La cantidad de reseñas de 5 estrellas fue: ",estrella_5)
print("La cantidad de reseñas de 4 estrellas fue: ",estrella_4)
print("La cantidad de reseñas de 3 estrellas fue: ",estrella_3)
print("La cantidad de reseñas de 2 estrellas fue: ",estrella_2)
print("La cantidad de reseñas de 1 estrellas fue: ",estrella_1)