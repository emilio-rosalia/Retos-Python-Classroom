# Reto 3
print('MAYORES QUE EL PRIMERO')
numeros_a_introducir = int(input('¿Cuántos valores vas a introducir? '))
if numeros_a_introducir < 1:
    print('¡Imposible!')
else:
    primer_numero = float(input('Escribe un número: '))
    for i in range(numeros_a_introducir-1):
        siguiente_numero = float(input(f'Escribe un número más grande que {primer_numero}: '))
        if siguiente_numero < primer_numero:
            print(f'¡{siguiente_numero} no es más grande que {primer_numero}!')
print('Gracias por su colaboración.')
