dias = 15
promedio =[]
while len(promedio)< dias: 
    try:
        temperatura_dias = int(input("Ingrese por favor la temperatura del dia en cuestion: "))
        promedio.append(temperatura_dias)
    except ValueError:
        print("ingrese un valor valido")
        break


valor_15_dias = sum(promedio) / dias
print("El promedio de temperatura fue de: ", valor_15_dias)
   