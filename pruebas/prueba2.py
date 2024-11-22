altura_persona = 0

while (True):
    # comment: 
    altura_persona = float(input("Ingrese por favor la altura de la persona a registar: "))
    if (altura_persona >=1.20):
        print("Usted puede ingresar a la atraccion")
    elif (altura_persona <1.20):
        print("Usted no puede ingresar a la atraccion") 
    
    respuesta = input("¿Desea ingresar otra persona? s/n: ")
    if (respuesta == "n"):
        # comment: 
        print("Gracias por itilizar este sistema, Adios")
        break
        
    # end if

     
