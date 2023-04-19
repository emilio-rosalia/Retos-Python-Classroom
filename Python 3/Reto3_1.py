# Reto 1
# Pedimos un número natural
numero = int(input('Introduce un número natural: '))
if numero%2 == 0: #Comprobamos si el resto de dividir por 2 es igual a 0
    print(f'El número {numero} es par.')
else:
    print(f'El número {numero} es inpar.')