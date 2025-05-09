#Ejercicio#4: Cálculo del consumo de combustible

#ingresamos kilometros y litros
kilometros = float(input("Ingrese la distancia recorrida en kilometros: "))

#Validamos que no se pueda ingresar un numero menor a 0
if kilometros < 0:
    print("Cantidad no valida, ingrese un valor mayor a 0")
    quit()

litros = float(input("Ingrese la cantidad de litros consumidos: "))

#Validamos que no se pueda ingresar un numero menor a 0
if litros < 0:
    print("Cantidad no valida, ingrese un valor mayor a 0")
    quit()

#divimos kilometros entre litros (rendimiento del vehiculo)
km_l = kilometros/litros

#definimos cuanto vale el litro
valor_litro = 47.84

#multiplicamos los litros por el precio por litro
gasto_combustible = litros*valor_litro

print(f"Distancia: {kilometros}, Litros: {litros}, Precio por litro: C${valor_litro}")
print(f"Rendimiento del vehiculo: {km_l}")
print(f"Gasto total de combustible: C${gasto_combustible}")