# Reto 3
# Halla la descomposición factorial de un número pedido.

# Pedimos un número hasta que de introduzcan solo digitos y no sea 0
numero = input('Introduce un número entero positivo: ')
while not (numero.isdigit() and numero !='0') :
    numero = input('Error !!\nIntroduce un número entero positivo: ')

numero=int(numero)

divisores = [] # Lista vacía donde vamos a guardar la descomposición factorial
i = 2 # El primer divisor primo de un número es el 2

while i <= numero: 
    if (numero % i == 0): # Comprobamos si i es divisor del número 
        divisores.append(i) # Lo guardamos
        numero = numero/i   # Dividimos el número por el divisor
    else: # Si no es divisor pruebo con el siguiente
        i = i+1       
    

print(f"Los divisores de {numero} son: {divisores}")