#Algoritmo de verificacion, si es mayor o menor de edad#
#AñoDeNacimiento Añoactual Resultado
Añoactual = 2024

AñoDeNacimiento = int(input(" Por favor ingrese su año de nacimiento: "))

Resultado = Añoactual - AñoDeNacimiento

if Resultado >= 18:
    print(" Usted es considerado en estos momentos como mayor de edad, Con una edad de:", Resultado, "Años")
    

else: 
    print ("Usted es considerado en estos momentos como menor de edad, Con una edad de: ", Resultado, "Años")
        