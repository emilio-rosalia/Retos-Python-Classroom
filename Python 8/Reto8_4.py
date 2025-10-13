#

def add_to_list(lista:list, item:str):
    """
    :param lista: list - Lista de cadena de caracteres.
    :param item: str - Cadena de texto.
    :return: list - Añadimos a la lista el elemento pasado con la primera letra en mayúsculas solo si no está en la listas. .
    """    
    if item.capitalize() in lista:
        return lista
    else:
        lista.append(item.capitalize())
        return lista



# Comprobamos que funciona 

lista = ["Hola", "Adios", "Paco"]
print(lista)
nueva_lista = add_to_list(lista, "hola")
print(nueva_lista)
nueva_lista = add_to_list(lista, "luis")
print(nueva_lista)
