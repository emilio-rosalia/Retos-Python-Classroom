# Reto 1

precio_docena = 7 # En esta variable guardamos el precio de la docena de huevos
# Pedimos el número de huevos que se quiere comprar
# Convertimos el valor introducido en un número entero
numero_de_huevos = int(input('¿Cuántos huevos quieres compar? '))
# Calculamos el precio de la compra en función de los valores anteriore
precio_compra = numero_de_huevos * precio_docena / 12
# Redondeamos el precio de compra a dos decimales
precio_compra = round(precio_compra,2)
# Mostramos el resultado por pantalla
print(f'El precio de {numero_de_huevos} es {precio_compra}')