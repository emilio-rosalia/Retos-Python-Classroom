# Reto 1
print('Número mayor')
numero1 = int(input('Introduce un número: '))
numero2 = int(input(f'Introduce un número mayor que {numero1}: '))
while numero1 >= numero2:
    numero2= int(input(f'{numero2} no es mayor que {numero1}. intentalo de nuevo: '))

print(f'\nLos números escritos son {numero1} y {numero2}.') # \n en una cadena de texto significa salto de línea
"""
Otra solución al reto 1
print('NÚMERO MAYOR')
primer_numero = float(input('Escribe un número: '))
# Asignamos a segundo número un número menor que el primero para que se cumpla la condición del While
# y se ejecute el bucle al menos una vez.
segundo_numero = primer_numero -1 
while segundo_numero < primer_numero :
    segundo_numero = float(input(f'Escribe un número meyort que {primer_numero}: '))"""