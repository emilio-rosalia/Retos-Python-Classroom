# Ejercicio 2
def multimplo (a,b):
    if b%a==0:
        return True
    else:
        return False
    
while True:
    try:
        a = int(input("Introduce un número: "))
        break
    except ValueError:
        print("Introduce un número entero")
while True:
    try:
        b = int(input(f"Introduce un núemro multiplo de {a}: "))
        if multimplo(a,b):
            print(f"{b} es múltiplo de {a}")
            break
        else:
            print(f"{b} no es múltiplo de {a}")
    except ValueError:
        print("Introduce un número entero")
