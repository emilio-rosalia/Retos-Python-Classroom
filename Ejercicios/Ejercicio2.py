# Ejercicio 2
# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas con o sin tilde).

# Solución
# Pedimos al usuario que introduzca una respuesta
respuesta = input("¿Desea continuar con el programa? (sí/no): ")
# Mientras la respuesta sea igual a "sí" (en minúsculas con o sin tilde)
while respuesta == "sí" or respuesta == "si":
    # Pedimos de nuevo la respuesta
    respuesta = input("¿Desea continuar con el programa? (sí/no): ")
# Si la respuesta no es igual a "sí"

print("Programa terminado")
