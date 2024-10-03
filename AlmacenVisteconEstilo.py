#Programa para Talla de ropa, segun tu estatura#
print ("Sea bienvenido a Almacenes Viste con estilo")
estatura = int(input("Por facor ingrese su estatura en centimetros: "))

if estatura <=150:
    print("Su talla de ropa respecto a su altura es de: S")
    
elif (150 > estatura <170):
        # comment: 
        print("Su talla de ropa respecto a su altura es de: M")

elif (170 >= estatura <180):
    # comment: 
    print("Su talla de ropa respecto a su altura es de: L")

if estatura >=180:
    print("Su talla de ropa respecto a su altura es de: XL")



