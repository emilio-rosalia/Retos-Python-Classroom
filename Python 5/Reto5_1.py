# Reto 1
print('NÚMERO MAYOR')
primer_numero = float(input('Escribe un número: '))
# Asignamos a segundo número un número menor que el primero para que se cumpla la condición del While
# y se ejecute el bucle al menos una vez.
segundo_numero = primer_numero -1 
while segundo_numero < primer_numero :
    segundo_numero = float(input(f'Escribe un número meyort que {primer_numero}: '))