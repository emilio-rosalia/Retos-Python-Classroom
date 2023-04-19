# Reto 3
numero = float(input('Introduce un número: '))
# En este reto usamos un elif porque solo se va a cumplir solo una de las opciones posibles.
if numero < -100:
    print('¿Por qué has elegido un número tan negativo?')
elif numero >= -100 and numero < 0:
    print('Has elegido un número negativo, interesante.')
elif numero >= 0 and numero < 100:
    print('Intereante número positivo.')
elif numero >= 100:
    print('¿Por qué eliges un número tan grande?')