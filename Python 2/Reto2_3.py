# Reto 3
# Modificamos el código a partir del reto 2 anterior para introdcir un código un segundo código de descuento
precio_docena = 7
# Creamos dos variables con los códigos 
codigo_descuento_1 = 'SuperTIC'
codigo_descuento_2 = 'PythonRosalia'
numero_de_huevos = int(input('¿Cuántos huevos quieres compar? '))
precio_compra = numero_de_huevos * precio_docena / 12
codigo_introducido = input('Introduce el código de descuento si lo tienes: ')
# Comprobamos si el código introducido es uno de los correctos
if codigo_introducido == codigo_descuento_1 or codigo_introducido == codigo_descuento_2:
    precio_compra = precio_compra * 0.9 
precio_compra = round(precio_compra,2)
print(f'El precio de {numero_de_huevos} es {precio_compra}')