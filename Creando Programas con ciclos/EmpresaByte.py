contador_portatil = 0
contador_camaras = 0
contador_otros_articulos = 0

ventas = 25
for i in range (ventas):
    # comment: 

 print("Bienvenido a la empresa byte, por favor revise su articulo a comprar")
 print("1. Linea de portatiles")
 print("2. Linea de Camaras")
 print("3. Otros Articulos")
 opcion = int(input("Ingrese por favor el numero del articulo, de acuerdo al menu: "))
 valor_articulo = int(input("Ingrese por favor el valor del articulo: "))
 
 if (opcion ==1):
    # comment: 
    contador_portatil +=1
    descuento = valor_articulo * 0.15
    valor_final = valor_articulo - descuento
    print("El valor del descuento es de: ", descuento)
    print("El valor final a pagar es de: ", valor_final, "pesos")
   
 elif (opcion == 2):
    # comment: 
    contador_camaras +=1
    descuento2 = valor_articulo * 0.05
    valor_final2 = valor_articulo - descuento2
    print("El valor de descuento es de: ", descuento2)
    print("El valor final a pagar es de: ", valor_final2, "pesos")

 elif (opcion == 3):
    contador_otros_articulos +=1
    descuento3 = valor_articulo * 0.02
    valor_final3 = valor_articulo - descuento3
    print("El valor del descuento es de: ", descuento3)
    print("El valor final a pagar es de: ", valor_final3, "pesos")


print("La cantida de portatiles vendidos es: ", contador_portatil)
print("La cantidad de camaras vendidas es: ", contador_camaras)
print("La cantidad de otros articulos vendidos es: ", contador_otros_articulos)


        





    
 
   

