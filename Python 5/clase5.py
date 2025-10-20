# Reto 5

import random

print('Voy a sumular el lanzamiento de un dado hasta que la suma de las tiradas llege a 21 o más.')

suma = 0
contador = 0
while suma < 21:
    contador += 1 # contador = contador +1
    tirada=random.randint(1,6)
    print(f'Ha salido un {tirada}.')
    suma += tirada # suma = suma + tirada
print('')
print(f'He tirado el dado {contador} veces y la suma total es {suma}.')