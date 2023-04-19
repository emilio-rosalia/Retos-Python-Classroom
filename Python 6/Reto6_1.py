# Reto 1
# Pedimos la cantidad de elementos que vamos a introducir
cantidad_de_elemetos_a_introducir = int(input('¿Cuántos elementos quieres introducir? '))
# Creamos la lista vacía
lista_de_elementos = []
# Hacemos un bucle que se repite el número de veces que indicó el usuario
for i in range(cantidad_de_elemetos_a_introducir):
    lista_de_elementos.append(input('¿Qué elemento quieres añadir a la lista? ')) # Añadimos a la lista el resultado del input

# Mostramos un listado con el contenido de la lista (no usamos print(lista) porque nos muesta la def de la lista con corchetes y comas)
# Para ello recorreremos la lista con un bucle para llamar elemento a elemento.

print('La lista está formada por', end='') # Quito el salto de línea y no dejo el espacio al final.
for i in range(len(lista_de_elementos)-1): # Todos los elementos menos el último porque el último lleva un punto al final.
    print(f' {lista_de_elementos[i]},', end='') # Elimino los saltos de línea y no dejo espacio al final por lo que tengo que añadir un espacio al principio.
# Mostramos el último número
print(f' {lista_de_elementos[len(lista_de_elementos)-1]}.') 
# Recuerda que las listas se empiezan a numerar en 0 porque que el último elemento tiene índice longitud de la lista menos 1
# Y que al usar la función range() creamos una lista que empieza en 0
# Reto ++ ¿Puedes hacer que el último elemento vaya precedido por la conjunción 'y' en vez de una coma?