# Contando de dos en dos

numero = int(input('Introduce un número positivo: '))
lista_de_pares = [] #lista donde añadiremos lo números pares
for i in range(numero):
    lista_de_pares.append(2*i)
print(f'Los pares pedidos son:{lista_de_pares}')