# Reto 2
numero = int(input('Introduce un número natural: '))
# En este reto tenemos encadenamos varios if uno detras de otro
# porque se puedes cumplir varias condiciones a la vez.
if numero%2 == 0: #Comprobamos si el resto de dividir por 2 es 0
    print(f'El número {numero} es divisible por 2.')
if numero%3 == 0: #Comprobamos si el resto de dividir por 3 es 0
    print(f'El número {numero} es divisible por 3.')
if numero%5 == 0: #Comprobamos si el resto de dividir por 5 es 0
    print(f'El número {numero} es divisible por 5.')
if numero%7 == 0: #Comprobamos si el resto de dividir por 7 es 0
    print(f'El número {numero} es divisible por 7.')
if numero%11 == 0: #Comprobamos si el resto de dividir por 11 es 0
    print(f'El número {numero} es divisible por 11.')
if numero%13 == 0: #Comprobamos si el resto de dividir por 13 es 0
    print(f'El número {numero} es divisible por 13.')