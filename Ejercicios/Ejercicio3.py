# Ejercicio 3
# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, hasta que se conteste exactamente no en minúsculas

# Solución
# Pedimos al usuario que introduzca una respuesta
respuesta = input("¿Desea continuar con el programa? (sí/no): ")
while respuesta != "no":
    # Pedimos de nuevo la respuesta
    respuesta = input("¿Desea continuar con el programa? (sí/no): ")

print("Programa terminado")
