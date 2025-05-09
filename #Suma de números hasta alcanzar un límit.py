#3Suma de números hasta alcanzar un límite

sum = 0

try:
    while True:
        numero = float(input("Ingresa un numero: "))
        sum = sum + numero
        if sum >= 100:
            break
    print(sum)
except ValueError:
    print("No se aceptan caracteres")
