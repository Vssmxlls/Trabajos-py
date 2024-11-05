accion_votos = 0
ciencia_ficcion_votos = 0

persona1 = input (" Por favor ingrese su preferencia de genero favorita entre accion y ciencia ficcion: ")
if persona1 == "accion":
    accion_votos += 1
else:
    # comment: 
    if persona1 == "ciencia ficcion":
        ciencia_ficcion_votos +=1


persona2 = input("Por favor ingrese su preferencia de genero favorita entre accion y ciencia ficcion:")
if persona2 == "accion":
    accion_votos +=1
else:
    # comment: 
    if persona2 == "ciencia ficcion":
        ciencia_ficcion_votos +=1

persona3 = input("Por favor ingrese su preferencia de genero favorita entre accion y ciencia ficcion:")
if persona3 == "accion":
    accion_votos +=1
else:
    # comment: 
    if persona3 == "ciencia ficcion":
        ciencia_ficcion_votos +=1

persona4 = input("Por favor ingrese su preferencia de genero favorita entre accion y ciencia ficcion:")
if persona4 == "accion":
    accion_votos +=1
else:
    # comment: 
    if persona4 == "ciencia ficcion":
        ciencia_ficcion_votos +=1

persona5 = input("Por favor ingrese su preferencia de genero favorita entre accion y ciencia ficcion:")
if persona2 == "accion":
    accion_votos +=1
else:
    # comment: 
    if persona2 == "ciencia ficcion":
        ciencia_ficcion_votos +=1

if ciencia_ficcion_votos > accion_votos:
    print("EL genero preferido es de ciencia ficcion con: ")
else:
    # comment: 
    if accion_votos > ciencia_ficcion_votos:
        print("El genero preferido es de accion")
