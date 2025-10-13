def calculo_dificil (lista:list, operacion:str):
    """
    :param lista: list - Lista de números enteros.
    :param operacion: str - Cadena de texto. SUM, MULT,MEDIA, ARMO, GEOM
    :return: int - Devuelve el resultado de la operación.
    """
    if operacion == "SUM": # Suma de todos los valores de la lista
        return sum(lista)
    elif operacion == "MULT": # Producto de todos los valores de la lista
        producto=1
        for i in lista:
            producto *= i
        return producto
    elif operacion == "MEDIA": # Media de todos los valores de la lista
        return sum(lista)/len(lista)
    elif operacion == "ARMO": # Media armónica de todos los valores de la lista
        media=0
        for i in lista:
            media += 1/i
        return len(lista)/media
        # return len(lista)/sum([1/i for i in lista]) Forma corta
    elif operacion == "GEOM": # Media geométrica de todos los valores de la lista
        producto=1
        for i in lista:
            producto *= i
        return producto**(1/len(lista))
        # return math.prod(lista)**(1/len(lista)) Forma corta
    else:   # Si no se especifica una operación válida, devuelve 0
        return 0
# Comprobamos que funciona correctamente
lista = [1,2,3,4,5]
print(calculo_dificil(lista, "SUM"))
print(calculo_dificil(lista, "MULT"))
print(calculo_dificil(lista, "MEDIA"))
print(calculo_dificil(lista, "ARMO"))
print(calculo_dificil(lista, "GEOM"))
