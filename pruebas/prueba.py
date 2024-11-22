estudiantes = 20
estudiantes_aprobados = 0
estudiantes_reprobados = 0
for i in range (estudiantes):
   nota_estudiante = float(input(f"Ingrese por favor la nota definitiva del estudiante: "))
   if nota_estudiante < 3.0:
      print("El estudiante no ha aprobado el curso")
      estudiantes_reprobados +=1
   elif (nota_estudiante >= 3.0 and nota_estudiante < 4.5):
      # comment: 
      estudiantes_aprobados +=1
      print("El estudiante ha aprobado el curso")
   elif (nota_estudiante >= 4.5):
         # comment: 
         estudiantes_aprobados +=1
         print("El estudiante ha aprobado con un desemepño superior")

print("La cantidad de estudiantes aprobados fue de:",estudiantes_aprobados)
 
print("La cantidad de estudiantes reprobados fue de: ", estudiantes_reprobados)
    
   

