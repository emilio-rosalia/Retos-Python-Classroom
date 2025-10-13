# Función que devuelve el núemero de veces que aparece las vocales en un texto
def contar_vocales(texto):
    texto = texto.lower()
    
    lista_a = ['a', 'á', 'à', 'ä', 'â', 'ã', 'å', 'æ']
    lista_e = ['e', 'é', 'è', 'ë', 'ê', 'ę', 'ė', 'ē', 'ĕ', 'ė', 'ę']
    lista_i = ['i', 'í', 'ì', 'ï', 'î', 'į', 'ī', 'ĭ']
    lista_o = ['o', 'ó', 'ò', 'ö', 'ô', 'õ', 'ø', 'œ', 'ō', 'ŏ', 'ő'] 
    lista_u = ['u', 'ú', 'ù', 'ü', 'û', 'ū', 'ŭ', 'ů', 'ű', 'ų']
    
    contador = [0,0,0,0,0]
    for letra in texto:
        if letra in lista_a:
            contador[0] += 1
        elif letra in lista_e:
            contador[1] += 1
        elif letra in lista_i:
            contador[2] += 1
        elif letra in lista_o:
            contador[3] += 1
        elif letra in lista_u:
            contador[4] += 1

    return contador

# Probramos la función con dos textos de ejemplo
texto1= "Hola, me llamo Juan"
print(texto1)
print(contar_vocales(texto1))
texto2 = 'María, Iria, ïrina, Óscar'
print(texto2)
print(contar_vocales(texto2))