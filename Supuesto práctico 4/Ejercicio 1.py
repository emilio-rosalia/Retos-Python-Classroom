# Sucesión de Collatz

def funcion_collatz (numero) :
    if numero % 2 == 0 :
        return numero // 2
    else :
        return 3*numero + 1
print('Sucesión de Collatz')
print('La sucesión de Collatz es una sucesión de números enteros positivos que se define de la siguiente manera: \n')
print('Si el número es par, se divide entre 2')
print('Si el número es impar, se multiplica por 3 y se le suma 1')
numero_de_terminos = 0
while True :
    try:
        valor_inicial = int(input('Introduce un número: '))
    except :
        print('Introduce un número entero, por favor')
    else :
        break

while numero_de_terminos <= 1 :
    try:
        numero_de_terminos = int(input('¿Cuántos términos de la sucesión de Collatz calculamos? '))
    except :
        print('Introduce un número entero positivo, por favor')


sucesion = []
sucesion.append(valor_inicial)

for i in range(numero_de_terminos-1) :
    valor_inicial = funcion_collatz(valor_inicial)
    sucesion.append(valor_inicial)

print(f'Los términos de la sucesión de Collatz son: {sucesion}')