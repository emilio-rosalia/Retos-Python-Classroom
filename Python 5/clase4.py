# Reto 4
limite = int(input('Escribe el valor límite: '))

while limite <= 0:
    limite = int(input(f'El valor límiete tiene que ser un nº positivo. Inténtelo de nuevo: '))
print('')
suma = 0
while suma < limite:
    numero = float(input('Introduce un número: '))
    suma = suma + numero # suma += numero
print('')
print(f'Has superado el límite, la suma de los números introducidos es {suma}.')