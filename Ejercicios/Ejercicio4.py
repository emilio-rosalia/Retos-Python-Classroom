# Ejercicio 4
# Escribe un programa que pida números hasta que se introduzca un número menor que el anterior. Luego decimos cuántos números se han introducido y cuál es la suma.

# Solución
# Pedimos al usuario que introduzca un número
num = int(input("Introduce un número: "))
# Inicializamos la variable suma a 0
# Pedimos al usuario que introduzca un número
num2 = int(input("Introduce un número mayor que " + str(num) + ": "))
# Mientras el segundo número sea mayor que el primero
# Inicializamos la variable contador a 2
suma = num
contador = 1
while num2 > num:
    # Añadimos 1 al contador
    contador += 1
    # Sumamos el número a la suma
    suma += num2
    # Igualamos el primer número al segundo
    num = num2
    # Pedimos al usuario que introduzca un número
    num2 = int(input("Introduce un número mayor que " + str(num) + ": "))
# Mostramos el resultado
print("Se han introducido", contador, "números y la suma total es", suma)