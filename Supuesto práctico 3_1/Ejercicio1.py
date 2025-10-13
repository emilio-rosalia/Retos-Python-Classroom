# Ejercicio 1
for i in range(4):
    numero = int(input('Introduce un número positivo: '))
    if numero <0:
        print('Había que introducir un número positivo.')
    elif numero >= 0 and numero < 100:
        print('El número es menor que una centena.')
    else:
        if numero%2 == 0 :
            print('El número es par.')
        else:
            print('El número es impar.')