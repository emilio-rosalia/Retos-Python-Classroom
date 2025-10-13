# Ejercicio 2
precio_metro = 2 # Precio en € de barnizar 1 m² sin IVA
presupuesto_disponible = float(input('Indique el presupuesto del que dispone: '))
ancho = float(input('Indica el ancho de la habitación en m: '))
largo = float(input('Indica el largo de la habitación en m: '))
coste_sin_iva = largo * ancho * precio_metro
coste_con_iva = largo * ancho * precio_metro * 1.21
if presupuesto_disponible > coste_con_iva :
    print('El presupuesto del que dispone es suficiente para el encargo.')
    respuesta = input('¿Desea formalizar el pedido? ')
    if respuesta == 'si' or respuesta =='Si'or respuesta=='sí' or respuesta=='Sí':
        print('Gracias por confiar en nosotros.')
        print(f'El coste del barnizado es {coste_sin_iva}€ más {coste_sin_iva*0.21}€ de IVA')
        print(f'El PVP es de {coste_con_iva}€')
    else:
        print('Lo lamento, lo dudes en volver a pedirnos presupuesto cuando quieras.')
else:
    print('Lamentablemente el presupueto del que dispone no es suficiente.')
    print(f'El coste total del barnizado sería de {coste_con_iva}€')