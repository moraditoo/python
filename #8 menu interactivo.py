#8 menu interactivo

from datetime import datetime

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

while True:
    try:
        print("\nEscoja una opcion")
        print("1. Saludar")
        print("2. Mostrar fecha")
        print("3. Salir")
        opcion = int(input("Ingrese el numero de opcion: "))
        if opcion == 1:
            nombre_de_usuario = input("Ingrese su nombre o usuario: ")
            print(f"Hola {nombre_de_usuario}")
        elif opcion == 2:
            print(f"Fecha actual: {fecha_formateada}")
        elif opcion == 3:
            print("Programa finalizado")
            break
        elif opcion > 3:
            print("Opcion entre en el 1 al 3")
        elif opcion < 1:
            print("Opcion entre en el 1 al 3")
    except ValueError:
        print("No decimales")
        