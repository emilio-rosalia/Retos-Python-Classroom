# Factorial
# Este programa calcula el factorial.
# Versión sencilla, no muestra por pantalla la operacion a realizar.

# Perdimos el número del que calcular el factorial y lo guardamos en la variable número.
numero=int(input('Introduce un número natural: '))
if numero < 0:
    print('¡Error! El número introducido es negativo.')
elif numero == 0:
    print('0!=1')
else: # Este caso correponde a que número 
    factorial = 1 # Iremos multiplicando esta variable por todos los números enteros hasta llegar a número.
    for i in range(numero):
        factorial=factorial*(i+1) # Recuerda que range(n) empieza en el 0 y termina en el n-1
    print(f'{numero}!={factorial}')