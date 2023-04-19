# Reto 5
print('MAYOR, MENOR Y MEDIA ARITMÉTICA')
suma_total = 0 # Sumaremos todos los valores 
# Hay un problema para elegir los valores iniciales para máximo y mínimo
valor_max = 0
valor_min = 0
# Pero eso lo arreglamos haciendo la prime
print('SUMA DE VALORES')
numeros_a_introducir = int(input('¿Cuántos valores vas a introducir? '))
if numeros_a_introducir < 1:
    print('¡Imposible!')
else:
    dato = float(input('Escriba el número 1: '))
    valor_max = dato
    valor_min = dato
    suma_total = dato
    for i in range(1,numeros_a_introducir):
        dato = float(input(f'Escriba el número {i+1}: '))
        suma_total = suma_total + dato
        # Comprobamos si hay que actualizar los valores de máximo o mínimo (Solo se puede dar uno de los dos casos)
        if dato > valor_max :
            valor_max = dato
        elif dato < valor_min:
            valor_min=dato
    media = suma_total / numeros_a_introducir
    print(f'El número más pequeño introducido es  {valor_min}')
    print(f'El número más grande introducido es {valor_max}')
    print(f'La media de los número introducidos es {media}')