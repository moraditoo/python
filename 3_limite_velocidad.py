#Ejercicio#3. Notificación de velocidad peligrosa en carretera

velocidad = float(input("Ingrese la velocidad en km/h: "))

if velocidad <= 0:
    print("Ingrese un numero mayor a 0")
    quit()

if velocidad >= 120:
    print("¡Reduzca la velocidad!")
else:
    print("Velocidad dentro del limite")
