#5 Adivinar un número

import random

numero_random = random.randint(1,10)
numero_ingresado = 1

try:
    while numero_random != numero_ingresado:
        numero_ingresado = int(input("\nIngresa un numero entre el 1 y 10: "))
        if numero_ingresado <= 0:
            print("Numeros entre el 1 y 10")
        elif numero_ingresado > 10:
            print("Numeros entre el 1 y 10")
        elif numero_random > numero_ingresado:
            print("El numero es mayor")
        elif numero_random < numero_ingresado:
            print("El numero es menor")
        elif numero_ingresado == numero_random:
            print("Felicidades, usted adivio el numero")
            break
except ValueError:
    print("No se aceptan caracteres ni decimales")