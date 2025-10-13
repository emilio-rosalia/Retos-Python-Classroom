# Conversor los puntos del jugador a la puntuación del juego
def resultado(a,b):
    if a==0:
        return '00'
    elif a==1:
        return '15'
    elif a==2:
        return '30'
    elif a>=3 and b<=3:
        return '40'
    elif a>=3 and b>=3:    
        if a==b:
            return 'deuce'
        elif a>b:
            return 'ventaja jugador 1'
        else:
            return 'ventaja jugador 2'
        
# Programa para llevare la puntucación de un partido de tenis
print('Programa para llevar la puntuación de un partido de tenis')
print('Escribe a si gana el primer juegador y b si gana el segundo.')
puntuacion = [0,0]
while abs(puntuacion[0]-puntuacion[1]) < 2 or max(puntuacion) < 4:
    punto=input('¿Quien ha ganado el punto? ')
    if punto == 'a':
        puntuacion[0] += 1
    elif punto == 'b':
        puntuacion[1] += 1
    
