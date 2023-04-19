# Reto 3
print('NÚMERO POSITIVOS')
cantidad_de_positivos_a_introducir = int(input('Escribe la cantidad de números positivos a escribir: '))
while cantidad_de_positivos_a_introducir < 0: # Comprobamos si el número dado es mayor que 0 y en caso contrario
    cantidad_de_positivos_a_introducir = int(input('La cantidad debe ser mayor que 0. Inténtelo de nuevo: '))
# Vamos a contar la cantidad números positivos introducido en la variable cantidad_de_positivos_a_introducidos
# Pediremos números hasta que el contador llegue a la cantidad pedida
cantidad_de_datos = 0 # Guaradamos los números introducidos
cantidad_de_positivos_introducidos = 0
dato = float(input('Escriba un número: '))
cantidad_de_datos += 1
if dato > 0:
    cantidad_de_positivos_introducidos += 1
while cantidad_de_positivos_introducidos < cantidad_de_positivos_a_introducir :
    dato = float(input('Escriba otro número: '))
    cantidad_de_datos += 1
    if dato > 0:
        cantidad_de_positivos_introducidos += 1
print(f'Ha escrito {cantidad_de_datos} números, {cantidad_de_positivos_introducidos} de ellos positivos.')