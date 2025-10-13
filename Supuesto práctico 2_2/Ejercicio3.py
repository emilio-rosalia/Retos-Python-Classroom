n = int(input("Ingrese la cantidad de términos a sumar: "))
suma = 0
for i in range(n):
    suma += 1/(2**i)
print("La suma es:", suma)