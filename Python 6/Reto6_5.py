# Reto 5
# La primera parte es identica al reto 4 pero es importante que en la lista se guarden los núemros en formato númerico ya que si los 
# guardamos como tipo STRING el número 11 está delante del 2

lista_de_numeros = []

nuevo_numero = input ('Introduce un nuevo número a guardar: ') 
while nuevo_numero != '.':
    if float(nuevo_numero) in lista_de_numeros: 
        print(f'El {nuevo_numero} ya está en la lista.')
    else:
        lista_de_numeros.append(float(nuevo_numero))
    nuevo_numero = input ('Introduce un nuevo número a guardar: ')
print('Siguiendo el orden de introducción de la lista.')
print('La lista está formada por', end='') 
for i in range(len(lista_de_numeros)-1):
    print(f' {lista_de_numeros[i]},', end='')
print(f' {lista_de_numeros[len(lista_de_numeros)-1]}.')

# Para ordenar la lista vamos a crear una lista vacía donde vamos a ir añadiendo los números ordenados de mayor a menor.
# Hacemos un duplicado de la lista_de_nuemeros para no perderla.
# Vamos a recorrer la lista duplicada para encontrar el número mayor, eliminarlo de la lista duplicada y añadirlo a la lista ordenada.
# Sabemos que en la lista no hay números repetidos. 
lista_de_numeros_ordenada = []
copia_lista_de_numeros = lista_de_numeros # Copia de la lista de núermos
# Buscamos el mayor número de la lista recorriendola.
# Repetimos el bucle las veces que teiene 
for i in range(len(copia_lista_de_numeros)): # Queremos repetir el siguiete código tantas veces como el 
    valor_max = copia_lista_de_numeros[0] # El primer candidato a valor máximo es el primer elemento de la lista
    for elemento in copia_lista_de_numeros: # Comprobamos todo los elementos de lista.
        if elemento > valor_max:
            valor_max = elemento
    lista_de_numeros_ordenada.append(valor_max) # Añadimos a la lista el valor más alto.
    copia_lista_de_numeros.remove(valor_max) # Eliminamos de la copia de la lista el valor más grande.

# Mostramos por pantalla la lista ordenada.
print('')
print('La lista ordenda de mayor a menor queda', end='') 
for i in range(len(lista_de_numeros_ordenada)-1):
    print(f' {lista_de_numeros_ordenada[i]},', end='')
print(f' {lista_de_numeros_ordenada[len(lista_de_numeros_ordenada)-1]}.')
