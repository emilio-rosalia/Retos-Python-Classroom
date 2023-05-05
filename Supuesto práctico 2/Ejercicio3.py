# Ejercicio 3
lista = []
longitud_lista = int(input('Introduce la longitud de la lista: '))
if longitud_lista <= 0:
    print('La próxima vez introduce un número mayor que cero.')
else:
    primer_elemnto = float(input('Introduce el primer elemento de la lista: '))
    lista.append(primer_elemnto)
    for i in range(longitud_lista-1):
        lista.append(3*lista[i]-5)
    print('La lista pedida es ', end='')
    print(lista)