# Ejercicio 3

suma=0
numero=int(input('Introduce un número positivo: '))

for i in range (numero):
    if (i+1)%2==0:
        suma += (i+1)

print(f"La suma de los pares menores que {numero} vale {suma}")