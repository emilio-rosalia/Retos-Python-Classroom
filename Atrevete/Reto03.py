# Reto 3
# Halla todos los divisores de un número introducido

# Pedimos un número hasta que de introduzcan solo digitos y no sea 0
numero = input('Introduce un número entero positivo: ')
while not (numero.isdigit() and numero !='0') :
    numero = input('Error !!\nIntroduce un número entero positivo: ')

numero=int(numero)

i = 2
while i**i <= numero:
    if anumero % i:
        print (i)
    i = i + 1
print(i)

print("Los divisores de", num, "son:")
divisores(num)