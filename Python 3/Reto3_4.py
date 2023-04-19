# Reto 4
# Pedimos dos números
numero_1 = float(input('Introduce un número'))
numero_2 = float(input('Introduce otro número'))
# Pedimos la suma de los dos números anteriores
suma = float(input('Introduce el valor de la suma de los números anteriores'))
# Comprobamos si el valor de suma es correcto.
if suma == numero_1 + numero_2 :
    print('¡Correcto!')
else:
    print('¡Revisa tus cuentas!')
    print(f'La suma de {numero_1} + {numero_2} es {numero_1+numero_2}')