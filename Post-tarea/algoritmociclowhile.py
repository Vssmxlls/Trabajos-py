while (True):
    # comment: 
    valor_cuenta = int(input("Ingrese el valor de la cuenta: "))
    print("1. Descuento del 15%")
    print("2. Descuento del 30%")

    eleccion = int(input("Segun el menu anterior, seleccione el descuento a aplicar para el cliente: "))

    if (eleccion == 1):
        # comment: 
        descuento1 = valor_cuenta * 0.15
        print("El valor del descuento a aplicar es de: ", descuento1)
    elif (eleccion == 2):
        # comment: 
        descuento2 = valor_cuenta * 0.30
        print("El valor del descuento a aplicar es de: ", descuento2)
   
   
    
    respuesta = input("Desea registar otro cliente?: ")
    if (respuesta =="no"):
        # comment: 
        print("Gracikas por utilizar este sistema de descuentos")
        break
    # end if


# end while