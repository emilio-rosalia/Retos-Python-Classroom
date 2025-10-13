texto = input('Introduce un texto: ')
letras_rosalianeas = {"r", "o", "s", "a", "l", "i", "a"}

texto = texto.lower()
for i in texto :
    letras_rosalianeas.discard(i)

if len(letras_rosalianeas) == 0 :
    print('El texto es Rosaliano')
else :
    print('El texto no es Rosaliano no se han usado las letras: ', end = '')
    for i in letras_rosalianeas :
        print(i, end = ' ')
