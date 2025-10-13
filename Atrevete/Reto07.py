import math

def funcion (x:float):
    return x**x - 10

def derivada (x:float):
    return x**x*(1+math.log(x))

def metodo_newton (apox:float) :
    new_aprox = apox - funcion(apox)/derivada(apox)
    return new_aprox

condicion = True
while condicion :
    try :
        apox = float(input('Introduce una aproximación de la solución: '))
    except :
        print('Por favor, introduce un número válido.')
    else :
        condicion = False

for i in range (10) :
    apox = metodo_newton(apox)
    print(apox)

