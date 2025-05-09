#4 Contador regresivo

try:
    numero = int(input("\nIngrese un numero positivo: "))
    if numero < 0:
        print("Ingresa un numero mayor o igual a 0")
        quit()
except ValueError:
    print("No se admiten caracteres")
    quit()

for i in range(numero, -1, -1):
    print(i)