print('Los cincuenta primeros terminos de la sucesión de fibonacci.')
# a_1 y a_2 almacenan los dos núemeros anteriores que se necesitan para
# calcular el siguiente término.
a_1=0
a_2=1
# Imprimo los dos primeros terminos de la sucesión.
print(f"{a_1}, {a_2}, ", end="")
# Repito el bucle 47 veces porque en la útima iteración no necesito la coma al final.
for turno in range(10000):
    a_3=a_1 +a_2
    print(a_3, end=", ")
    # Guardo en a_1 y a_2 los terminos para calcular el termino siguiente.
    a_1 = a_2
    a_2 = a_3
# Calculo el último termino de forma separa para poner un punto en vez de una coma.
a_3=a_1 +a_2
print(f"{a_3}.")