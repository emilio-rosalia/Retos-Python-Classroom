deuda = 50
while deuda > 0:
    print(f"Deuda actual: {deuda}€")
    pago = float(input("Introduce el pago: "))
    deuda -= pago
    

print("La deuda ha sido saldada")
if deuda < 0:
    print(f"La vuelta es de: {abs(deuda)}€")