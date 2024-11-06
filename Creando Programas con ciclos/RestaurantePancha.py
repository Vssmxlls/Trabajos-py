while (True):
    # comment:
    valor_cuenta = int(input("Ingrese el valor de la cuenta a pagar del cliente: "))
    propina_sugerida = valor_cuenta * 0.15
    print("El valor de la propina sugerida es de: ", propina_sugerida, "pesos")

    respuesta = input("¿Desea registrar otro cliente?: ")

    if respuesta == "no":
        print("Sesion terminada, Muchas gracias por utilizar el sistema de propinas ")
        break
