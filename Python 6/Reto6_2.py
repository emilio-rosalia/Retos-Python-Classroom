# Reto 2
# Pedimos la cantidad de palabras que vamos a introducir
cantidad_de_palabras_a_introducir = int(input('Díagame cuantas palabras tiene la lista '))
# Creamos la lista de palabras vacía
lista_de_palabras = []
for i in range(cantidad_de_palabras_a_introducir):
    lista_de_palabras.append(input(f'Dígame la palabra {i+1}: '))

print(f'La lista creada es {lista_de_palabras}')
palabra_a_buscar = input('Dígame la plabra a buscar: ')

if lista_de_palabras.count(palabra_a_buscar) == 0:
    print(f"La palabra '{palabra_a_buscar}' no aparece en la lista.")
elif lista_de_palabras.count(palabra_a_buscar) == 1:
    print(f"La palabra '{palabra_a_buscar}' aparece una vez en la lista.")
elif lista_de_palabras.count(palabra_a_buscar) > 1:
    print(f"La palabra '{palabra_a_buscar}' aparece {lista_de_palabras.count(palabra_a_buscar)} veces en la lista.")