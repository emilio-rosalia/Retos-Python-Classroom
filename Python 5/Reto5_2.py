# Reto 2
print('NÚMEROS MAYORES')
numero_pedido_1 = numero_pedido_2 = float(input('Escribe un número: ')) # Se pueden igualar dos variables con un tercer valor en una línea.
while numero_pedido_1 <= numero_pedido_2 :
    numero_pedido_1 = numero_pedido_2
    numero_pedido_2 = float(input(f'Escribe un número mayor que {numero_pedido_1}: '))
print(f'{numero_pedido_2} no  es mayor que {numero_pedido_1}.')