# Ejercicio
print('VELOCIDAD')
velocidad = 1 # Valor inicial, en metros por segundo (m/s).
# Es 1 porque voy a multiplicarla por la distancia y dividirlo por el tiempo.
unidad_distancia = input('Unidad de distancia (m o km): ')
if unidad_distancia =='m' or unidad_distancia=='km': #Si la undidad es introducida correctamente seguimos con el programa
    distancia_recorida =float(input('Distancia recorrida: '))
    if unidad_distancia == 'm':
        velocidad = distancia_recorida
    elif unidad_distancia == 'km': #Convertimos la distanca a metros
        velocidad = distancia_recorida * 1000
    # Como hemos introducido un valor para la unidad de distancia preguntamos por el tiempo.
    unidad_tiempo = input('Unidad de tiempo (s o h): ')
    if unidad_tiempo == 's' or unidad_tiempo == 'h':#Si la undidad es introducida correctamente seguimos con el programa
        tiempo_empleado = float(input('Tiemplo empleado: '))
        if unidad_tiempo == 's':
            velocidad = velocidad/tiempo_empleado
        else: #Convertimos el tiempo a segundos.
            velocidad = velocidad/(tiempo_empleado * 3600)
        # Mostramos el mensaje con los datos. Recuerda el factor de conversion de m/s a k/h es 3.6
        print(f'Si ha recorrido {distancia_recorida} {unidad_distancia} en {tiempo_empleado} {unidad_tiempo} su velocidad ha sido {velocidad:.2f} m/s ({velocidad*3.6:.2f} km/h)')
    else: #Si la unidad introducida no es correcta mensaje y fin.
        print('La unidad de tiempo que ha indicado no es s o h')
else: #Si la unidad introducida no es correcta mensaje y fin.
    print('La unidad de distancia que ha indicado no es m o km.')