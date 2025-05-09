#6 Promedio de calificaciones

suma = 0
calilificacion = 0 
contador = 0


try:
    while True:
        calificacion = float(input("Ingrese la calificacion (-1 para terminar): "))
        if calificacion == -1:
            break
        suma = suma + calificacion
        contador +=1    
    promedio = suma // contador
    print(f"El promedio de las calificaiones es {promedio}")
except ValueError:
    print("No se aceptan caracteres")


