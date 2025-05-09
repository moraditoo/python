#Ejercicio#9. Encontrar el mayor de tres números

# Ingresar los tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Verificar si los tres son iguales
if num1 == num2 == num3:
    print("Los números son iguales.")
else:
    # Comparar para encontrar el mayor
    if num1 >= num2:
        if num1 >= num3:
            mayor = num1
        else:
            mayor = num3
    else:
        if num2 >= num3:
            mayor = num2
        else:
            mayor = num3
    print(f"El número mayor es: {mayor}")