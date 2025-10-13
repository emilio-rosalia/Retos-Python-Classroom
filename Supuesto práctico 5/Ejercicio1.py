# Ejercicio 1-a
def es_punta_de_flecha(palabra:str):
    if " " in palabra:
        return False
    else:
        if len(palabra) % 2 == 0:
            return False
        else:
            if palabra[0].lower() == palabra[-1].lower():
                return True
            else:
                return False        
        
# Ejercicio 1-b
condicion = True
while condicion:
    respuesta = input("Ingrese una palabra: ")
    if es_punta_de_flecha(respuesta):
        print("La palabra es punta de flecha")
        condicion = False
    else:
        print("La palabra no es punta de flecha")