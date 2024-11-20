def clasificacion_de_glucosa(nivel):
    if nivel <= 75:
        return "Hipoglucemia"  
    elif nivel > 75 & nivel < 105:
        return "Normal" 
    elif 105 <= nivel < 126:
        return "Prediabetes" 
    else:
        return "Diabetes"  

nivel = int(input("Por favor ingrese el nivel de glucosa del paciente en ml: "))
resultado = clasificacion_de_glucosa(nivel)
print("Su clasificación de glucosa de acuerdo a su nivel es:", resultado)






















































































 
 

 
   