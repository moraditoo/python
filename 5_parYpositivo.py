#Ejercicio#5. Verificar si un número es par y es positivo

numero = int(input("Ingrese un numero: "))

if numero < 0:
    print("Numero negativo")
    quit()
elif numero == 0:
    print("Numero no valido")
    quit()
if numero > 0 and numero % 2 == 0:
    print("Numero positivo")
    print("Numero par")