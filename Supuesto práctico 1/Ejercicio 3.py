# Adivina adivinanza
numero_secreto = 33 # Aquí voy a guardar el número 
print('Adivina adivinanza')
print('Intenta adivinar el número que he pensado.')
intento = numero_secreto +1 # Aquí voy a guardar el número introducido por el usuario. En primera instancia le asigno me aseguro de que intento es distinto de numero_secreto sea cua sea el valor que tenga.
while numero_secreto != intento:
    intento = int(input('Di un número: '))
    if intento < numero_secreto:
        print('Te has quedado corto')
    elif intento > numero_secreto:
        print('Te has pasado.')
    else:
        print('¡Enhorabuena! Por fín lo has conseguido.')
