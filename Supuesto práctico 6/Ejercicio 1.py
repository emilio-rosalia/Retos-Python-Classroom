# Ejercicio 1

# Pedimos una palabra
palabra=input("Introduce una palabra o un breve texto: ")

# Pedimos una letra
condicion = True
while condicion:
    letra = input("Introduce una letra: ")
    # Si la letra tiene una longitud mayor a 1 o es un " " pedimos otra letra
    if len(letra) > 1 or letra == " ":
        print("Introduce una única letra.")
    else:
        condicion = False

# Contamos cuantas veces se repite la letra en la palabra
contador_letra = 0
for i in palabra:
    if i == letra:
        contador_letra += 1

print(f"La letra {letra} se repite {contador_letra} veces en: {palabra}")