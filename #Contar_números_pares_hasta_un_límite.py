#Contar números pares hasta un límite

contador = 0

try:
    numero = int(input("\nIngrese el limite: "))
    if numero <= 0:
        print("Ingresa un numero mayor o igual a 1")
        quit()
except ValueError:
    print("No se permiten caracteres")
    quit()


while contador <= numero:
    if contador % 2 == 0:
        print(f"{contador}")
    contador += 1  


    