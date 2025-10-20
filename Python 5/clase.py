print('Números mayores')
numero1= float(input('Introduce un número: '))
numero2 = numero1+1
while numero1 < numero2:
    numero2 = float(input(f'Introduce un número mayor que {numero1:}: '))
    if numero2 > numero1:
        numero1 = numero2 # para actualizar el valor de numero1
        numero2 = numero2+1 # Para poder entrar en el bucle
print(f'{numero2} no es mayor que {numero1}')
