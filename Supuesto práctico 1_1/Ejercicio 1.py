# Ejercicio 1
print('Bienvenido al Hotel de los Números Naturales')
print('Donde todos los números enteros tienen una habitación')

# En la variable huesped guardaremos el núemro que se va se va a alojar en el hotel
huesped = int(input('¿Cómo se llama? '))
# En la variable habitacion guardaremos el número de la habitación que le corresponde
if huesped >= 0:
    habitacion = 2*huesped
else:
    habitacion = -2*huesped-1
print(f'Encantado de tenerle en nuestro Hotel {huesped} su habitación es {habitacion}.')
print('Espero que disfrute de su estancia.')