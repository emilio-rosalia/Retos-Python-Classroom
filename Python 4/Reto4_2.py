# Reto 2
print('Divisores')
numero = int(input('Escribe un número entero mayor que cero: '))
# Comprobamos si el número introducido es mayor que cero
if numero <= 0:
    print('¡Le he pedido un entero mayor que cero!')
else:
    print(f'Los divisores de {numero} son', end='') # Esto se imprime una única vez
    for i in range(numero): # Probamos si se puede dividir el número dado por todos los números menores
        # Recuerda que empiza en 0 y termina en numero-1, por este motivo le sumo 1
        if numero % (i+1) == 0 : # Comprobamos si divide al número
            print(f' {i+1}', end='')

# Reto 2.1
# Separamos los divisores por comas.
print('')
print('Divisores 2.1')
#numero = int(input('Escribe un número entero mayor que cero: '))
# Comprobamos si el número introducido es mayor que cero
if numero <= 0:
    print('¡Le he pedido un entero mayor que cero!')
else:
    print(f'Los divisores de {numero} son', end='') # Esto se imprime una única vez
    for i in range(numero): # Probamos si se puede dividir el número dado por todos los números menores
        # Recuerda que empiza en 0 y termina en numero-1, por este motivo le sumo 1
        if numero % (i+1) == 0 : # Comprobamos 
            print(f', {i+1}', end='')
    print('.')