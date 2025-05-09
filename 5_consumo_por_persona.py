#Ejercicio#5: Cálculo del consumo de agua por persona

#Se ingresa el total de litros consumidos en un mes en una vivienda
litrosconsumidos = float(input("Ingrese la cantidad total de litros consumidos en el mes: "))

#Validamos que no pueda ser un numero menor que 0
if litrosconsumidos < 0:
    print("Cantidad no valida, ingrese un numero mayor a 0")
    quit()

#Se ingresa la cantidad de personas que viven en la casa
personas = int(input("Ingrese la cantidad de personas que viven en la casa: "))

#Validamos que no pueda ser un numero menor o igual a 0
if personas <= 0:
    print("Cantidad no valida, ingrese un numero mayor o igual")
    quit()

#Calculamos el consumo mensual por persona
consumomensual = litrosconsumidos/personas

#Calculamos el consumo diario por persona
consumodiario = consumomensual/30

print(f"Consumo total del mes: {litrosconsumidos}L")
print(f"Viven {personas} en la casa")
print(f"El consumo mensual es de {consumomensual:.2f}L y consumo diario {consumodiario:.2f}L por persona")