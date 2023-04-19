import random
print()
suma=0
numero_tiradas=0
print("Voy a lanzar el dado hasta que la suma de las tiradas se mayor o igual a 21.")
while suma<21 :
    dado=random.randrange(1, 6)
    print(f"He obtenido un {dado}")
    suma+=dado
    numero_tiradas+=1

print(f"He lanzado el dado {numero_tiradas} y la suma de los resultados es {suma}.")