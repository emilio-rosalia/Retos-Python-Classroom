# Tabla de multiplicar
print('Tabla de multiplicar')
numero_tabla = input('De que número quieres la tabla de multiplicar: ')
while not numero_tabla.isdigit():
    numero_tabla = input('Error !!\nDe que número quieres la tabla de multiplicar: ')
numero_tabla = int(numero_tabla)
for i in range(1,11):
    print(f"{numero_tabla} x {i} = {numero_tabla*i}")
