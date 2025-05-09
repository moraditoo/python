def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ingrese el valor de la base: "))
exponente = int(input("Ingrese el valor de el exponente: "))

print("base^exponente =", potencia(base, exponente))  # Salida: 8
