# Ejercicio 1
numero = int(input('Introduce un número: '))
if numero<0:
    print('La próxima vez introduce un número positivo.')
elif numero%2==0:
    print(f'Has introducido el {numero} que es par y su mitad es {int(numero/2)}')
elif numero%2!=0:
    print(f'Si multiplicamos {numero} por 3 y le restamos 1 obtenemos {3*numero-1}')