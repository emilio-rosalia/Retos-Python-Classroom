# Factorial
# Este programa calcula el factorial.
# Versión completa.

# Perdimos el número del que calcular el factorial y lo guardamos en la variable número.
numero=int(input('Introduce un número natural: '))
if numero < 0:
    print('¡Error! El número introducido es negativo.')
elif numero == 0:
    print('0!=1')
else: # Este caso correponde a que número 
    factorial = 1 # Iremos multiplicando esta variable por todos los números enteros hasta llegar a número.
    print(f'{numero}!=1',end='')
    for i in range(2, numero+1): # Con este range i tomorá todos los valores entre 2 y número
        print(f'·{i}',end='')
        factorial=factorial*i
    print(f'={factorial}')