
import random

def obtener_palabra():
    palabras = ["python", "ahorcado", "programacion", "juego", "computadora"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos > 0:
        print("\n" + mostrar_tablero(palabra, letras_adivinadas))
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        elif letra in palabra:
            print("¡Bien hecho!")
            letras_adivinadas.append(letra)
        else:
            print("Letra incorrecta.")
            intentos -= 1
            letras_adivinadas.append(letra)

        if all(l in letras_adivinadas for l in palabra):
            print("\n¡Felicidades! Adivinaste la palabra:", palabra)
            break
    else:
        print("\n¡Te has quedado sin intentos! La palabra era:", palabra)

ahorcado()


