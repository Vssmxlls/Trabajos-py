horas_personas = []
personas_encuestadas = 0

while personas_encuestadas <= 15:
    try:
        horas = int(input("Ingrese por favor la cantidad de horas gastadas el día domingo en la plataforma de Netflix: "))
        horas_personas.append(horas)
        personas_encuestadas += 1
    except ValueError:
        print("Por favor, ingrese un número válido.")

promedio_horas = sum(horas_personas) / personas_encuestadas

# Mostrar resultados
print("\nLas horas ingresadas por las 15 personas son:", horas_personas)
print("El promedio de horas es:", promedio_horas)
