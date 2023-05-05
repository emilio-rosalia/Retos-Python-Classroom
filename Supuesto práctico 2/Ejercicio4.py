# Ejercicio 4
numero_de_supuestos_practicos=0
respuesta = 'no'
while respuesta != '10' and respuesta != 'diez':
    respuesta = input('¿Qué nota quieres sacar en TIC? ')
    numero_de_supuestos_practicos += 1
print(f'Enhorabuena, fruto de un gran trabajo. Has necesitado {numero_de_supuestos_practicos} supuestos prácticos.')