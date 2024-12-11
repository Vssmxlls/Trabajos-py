def clasificacion_descuento (dias):
    if (dias == 1):
        return "Montañismo"
        # comment: 
    # end if
    elif (dias == 2):
        return "Tenis"
    elif (dias == 3):
        # comment: 
        return "Ciclismo"
    elif (dias == 4):
        # comment: 
        return "Atletismo"
    elif (dias == 5):
        return "Futbol"
    elif (dias == 6):
        return "Natacion"
    else:
        # comment: 
        print("Dia no valido")






print("Bienvenido al menu")
print("1.Lunes")
print("2.Martes")
print("3.Miercoles")
print("4.Jueves")
print("5.Viernes")
print("6.Sabado")
try:

 dias = int(input("Ingrese por favor el numero del dia, de acuerdo al menu: "))
 deporte_descuento = clasificacion_descuento(dias)
 print("El deporte con descuento del dia de hoy es: ", deporte_descuento)
except ValueError:
    print("Por favor ingrese un valor valido")