print(" Sea bienvenido al menu")

nombre = input("Por favor ingrese su nombre: ")
edad = int(input ("Por favor ingrese su edad: "))
if edad <18:
    exit

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

        resultadosuma = a + b

        print("el resultado es: ", resultadosuma)
    
    elif operacion == "resta":
        
        resultado2 = a - b

        print("el resultado es: ", resultado2)

    elif operacion == "multiplicacion":

        resultado3 = a * b

        print("el resultado es: ", resultado3)

        
    
    elif operacion == "division":
        resutado5 = a / b

        print("el resultado es:", resultado5)

elif opcion == 2:
    print("!Hola!", nombre, "tu edad es de: ", edad)


opcional= input ("Desea ver los resultados multples?: ")
if opcional =="si" or "y":
    print("los resultados de todas las operaciones fueron: ")

    print("Resta: ",resultado2)
    print("Multiplicacion: ", resultado3)
    print("Division: ", resultado5)

elif opcional == "no" or "n":

    exit
   

    