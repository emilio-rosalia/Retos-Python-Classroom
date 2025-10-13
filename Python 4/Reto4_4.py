# Reto 4
suma_total = 0 # Creamos una variable donde vamos a guardar la suma de los números intoducimos
print('SUMA DE VALORES')
numeros_a_introducir = int(input('¿Cuántos valores vas a introducir? '))
if numeros_a_introducir < 1:
    print('¡Imposible!')
else:
    for i in range(numeros_a_introducir):
        dato = float(input(f'Escriba el número {i+1}: '))
        suma_total = suma_total + dato # suma_total += dato
    print(f'La suma total de los número introducidos es {suma_total}')