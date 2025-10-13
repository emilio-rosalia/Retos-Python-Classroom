# Reto 4

lista_de_numeros = []

nuevo_numero = input ('Introduce un nuevo número a guardar: ') # Dejamos el input como un STRING para poder manejar el punto.
while nuevo_numero != '.':
    if float(nuevo_numero) in lista_de_numeros: # Comprobamos si un número está en la lista.
        print(f'El {nuevo_numero} ya está en la lista.')
    else:
        lista_de_numeros.append(float(nuevo_numero)) # Guardamos el nuevo dato en la lista convertido en números
    nuevo_numero = input ('Introduce un nuevo número a guardar: ')

# print(lista_de_numeros) Forma cutre, mucho mejor hacerlo como en el reto 1
print('La lista está formada por', end='') 
for i in range(len(lista_de_numeros)-1):
    print(f' {lista_de_numeros[i]},', end='')
# Mostramos el último número
print(f' {lista_de_numeros[len(lista_de_numeros)-1]}.')

# Ordenamos la lista
lista_de_numeros.sort()
print('La lista ordenada es', end='')