# Reto 2 
# Modificamos el código a partir del reto anterior para introdcir un código
# de descuento
precio_docena = 7
descuento = 10 # porcentaje de descuento
numero_de_huevos = int(input('¿Cuántos huevos quieres compar? '))
precio_compra = numero_de_huevos * precio_docena / 12
# Preguntamos por el código de descuento
codigo_introducido = input('Introduce el código de descuento si lo tienes: ')
# Comprobamos si el código introducido es correcto
if codigo_introducido == 'SuperTIC':
    precio_compra = precio_compra * (1 - descuento / 100) # Cambiamos aplicamos el descuento de 10%
precio_compra = round(precio_compra,2) # Redondeamos el precio a dos decimales antes de mostrarlo
print(f'El precio de {numero_de_huevos} es {precio_compra}€')