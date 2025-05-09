#Tabla de multiplicar

try:
    numero = int(input("Ingrese un numero entero y positivo: "))
    contador = 0
    for i in range(1,11):
        resultado = numero * i
        contador = contador + 1
        print(f"{contador}. {resultado}")
    if numero <= 0:
        print("Ingresa un numero mayor o igual a 1")
        quit()
except ValueError:
    print("No puedes ingresar caracteres")