print('HASTA EL LÍMITE')
valor_limite = float(input('Escriba el valor límite: '))
while valor_limite <= 0:
    valor_limite = float(input('El límite debe ser mayor que 0. Inténtelo de nuevo: '))
print('') # Para añador dos saltos de líneas
print('')
suma = 0 # Guarda el suma de todos los número que se introduciran a continueación.
suma = float(input('Escriba un número: ')) # Guardamos el primer número.
while suma <= valor_limite : # Repetimos hasta que suma supere el valor del límite.
    dato = float(input('Escriba otro número: '))
    suma += dato
print('')
print('')
print(f'Ha superado el límite. La suma de los núemdo introducidos es {suma}.')
