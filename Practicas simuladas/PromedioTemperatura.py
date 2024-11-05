#Estudio de temperatura por la Escuela ECAPMA de la UNAD# 
#Dia1, Dia2, Dia3, Dia4, Dia5, Promedio

Dia1 = int(input("Ingrese por favor la temperatura del dia 1: "))
Dia2 = int(input("Ingrese por favor la temperatura del dia 2: "))
Dia3 = int(input("Ingrese por favor la temperatura del dia 3: "))
Dia4 = int(input("Ingrese por favor la temperatura del dia 4: "))
Dia5 = int(input("Ingrese por favor la temperatura del dia 5: "))

Promedio = (Dia1 + Dia2 + Dia3 + Dia4 + Dia5)/5

if Promedio >= 22:
    print("El clima ha sido calido durantes estos 5 dias con un promedio de : ", Promedio, "Grados Centigrados")
   
else:
        print("El clima ha sido frio durante estos 5 dias con un promedio de :", Promedio, "Grados Centigrados")
    # comment: 
      



