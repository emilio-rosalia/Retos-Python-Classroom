# Reto 1
numero_1 = int(input('Escribe un número entero: '))
# Pedimos un número mayor que el anterior 
numero_2 = int(input(f'Escribe un número entero mayor que {numero_1}: '))
# Comprobamos si el segundo número es mayor
if numero_1 > numero_2: # Si el primer número es mayor mostramos un mensaje de error
    print(f'¡Le he pedido un núemro mayor o igual que {numero_1}!')
else: # En caso contrario hacemos el bucle para mostrar la paridad de todos lo números comprendidos
    for i in range(numero_1, numero_2+1): # Recuerda que el último valor de range el anterior ind
        if i % 2 == 0:
            print(f'El número {i} es par')
        else:
            print(f'El número {i} es impar')