def siguiente_termino(n:float):
    return n**2-3*n

# Pedimos un número al usuario
sucesion = []
condicion = True
while condicion:
    try:
        primer_termino = float(input("Ingrese el primer términa de la sucesión: "))
        condicion = False
    except:
        print("El número ingresado no es válido")
condicion = True
while condicion:
    try:
        cantidad_terminos = int(input("Ingrese la cantidad de términos que desea: "))
        if cantidad_terminos > 0:
            condicion = False
        else:
            print("La cantidad de términos debe ser mayor que cero.")
    except:
        print("La cantidad de términos debe ser un número entero positivo.")

sucesion.append(primer_termino)
for i in range(cantidad_terminos-1):
    sucesion.append(siguiente_termino(sucesion[i]))

print(sucesion)