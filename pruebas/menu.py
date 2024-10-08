print(" Sea bienvenido al menu")

nombre = input("Por favor ingrese su nombre: ")
edad = input ("Por favor ingrese su edad: ")

print("Hola",nombre, "Por favor seleccione algunas de las siguientes opciones")

print("1. Calcular algo")
print("2. Saludo")

opcion = int(input("Opcion a elegir: "))


if opcion == 1:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    print ("¿Que deseas hacer?: " )
    suma= print("- Suma")
    resta= print("- Resta")
    division= print("- Division")
    multiplicacion= print("- Multiplicacion")
   
    operacion= input("Escriba alguna de las opciones anteriores: ")

    if operacion == "suma":

        resultado = a + b

        print("el resultado es: ", resultado)
    
    elif operacion == "resta":
        
        resultado2 = a - b

        print("el resultado es: ", resultado2)

    elif operacion == "multiplicacion":

        resultado3 = a * b

        print("el resultado es: ", resultado3)

        
    
    elif operacion == "division":
        resutado4 == a / b

        print("el resultado es:", resultado4)




    
    
    
    

    




    


    
    
 
      
    




elif opcion == 2:
    print("!Hola!", nombre, "tu edad es de: ", edad)