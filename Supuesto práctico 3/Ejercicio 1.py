#  n primeros múltiplos de 7
dato_correcto = False
while not dato_correcto:
    try:
        n = int(input("Introduce un número entero positivo: "))
        if n > 0:
            dato_correcto = True
        else:
            print("El número debe ser positivo")
    except ValueError:
        print("El valor introducido no es un número entero")

lista_multiplos = []
for i in range(n):
    lista_multiplos.append(7*i)

print(lista_multiplos)
