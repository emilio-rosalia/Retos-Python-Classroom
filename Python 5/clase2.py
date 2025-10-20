# Reto 3
cantidad_numeros_a_pedir = int(input('¿Cuántos números positivos quieres introducir? '))

while cantidad_numeros_a_pedir <= 0:
    cantidad_numeros_a_pedir = int(input(f'{cantidad_numeros_a_pedir} no es un nº positivo. Inténtelo de nuevo: '))

contador_de_positivos_introducidos = 0 # Para llevar la cuenta de los números positivos que se van introduciendo
contador_de_intentos = 0 # Para llevar la cuenta de los intentos totales
while contador_de_positivos_introducidos < cantidad_numeros_a_pedir:
    numero = int(input('Introduce un nº positivo: '))
    contador_de_intentos += 1
    if numero > 0:
        contador_de_positivos_introducidos += 1 

print(f'Has escrito {contador_de_intentos} números de los cuales {contador_de_positivos_introducidos} son positivos.')

