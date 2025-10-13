# Reto 5
# Pedimos dos números
numero_1 = float(input('Introduce un número: ')) # Usamos float para permitir número decimales
numero_2 = float(input(f'Introduce un número menor que {numero_1}: '))
if numero_2 > numero_1 : # Si el 2º número es mayor que el primero mostramos un mensaje de error.
    print(f'Tenías que introducir un número menor que {numero_1}')
else:
    # Si el 2º número es menor que el primero pedirmos el sesultado de la resta de ambos números.
    diferencia = float(input(f'Introduce el resultado de restar {numero_2} a {numero_1}: '))
    if diferencia == numero_1 - numero_2:
        print('¡Correcto!')
    else:
        print('Eso no es correcto.')
        print(f'El resultadode restar {numero_2} a {numero_1} es {numero_1-numero_2}')