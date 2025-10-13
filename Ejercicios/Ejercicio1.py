# Ejercicio 1
# Haz un programa que calcule los n primeros múltiplos de un número dado.
multiplo = int(input("Introduce el número del que quieres saber los múltiplos: "))
n = int(input("Introduce cuántos múltiplos quieres saber: "))
print(f"Los {n} primeros múltiplos de {multiplo} son: ")
for i in range(n):
    print(multiplo * i, end=" ") # Multiplicamos el número por el rango de 1 a n+1
