# Solicitar el nombre y apellido por separado
nombre = input("Ingrese su nombre: ")
if not nombre.strip():
    print("Error: El nombre no puede estar vacío.")
    exit()

apellido = input("Ingrese su apellido: ")
if not apellido.strip():
    print("Error: El apellido no puede estar vacío.")
    exit()

resultado = nombre[0].upper() + ". " + apellido.capitalize()
print("El resultado es:", resultado)