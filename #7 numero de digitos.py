#7 numero de digitos

contador = 0 

try:
    numero = int(input("Ingrese un numero entero y positivo: "))
except ValueError:
    print("No se aceptan caracteres ni decimales")

while numero > 0:
    numero = numero // 10
    contador +=1

print(f"El numero de digitos es igual a {contador}")
