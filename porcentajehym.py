#2. Algoritmo para calcular el porcentaje de mujeres y varones en un aula.
varones = int(input("Ingrese la cantidad de varones: "))
mujeres = int(input("Ingrese la cantidad de mujeres: "))
total = varones+mujeres
porcentajevarones = (varones/total)*100
porcentajemujeres = (mujeres/total)*100
print("El porcentaje de varones es: ", porcentajevarones, "%")
print(" El porcentaje de mujeres es:", porcentajemujeres, "%")