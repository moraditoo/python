#Ejercicio#8. Verificación de inicio de sesión

usuario = input("Ingrese su usuario: ")

if usuario == "admin":
    print("Usuario corercto")
else:
    print("Usuario incorrecto, vuelva a intentarlo")
    quit()

contrasenia = input("Ingrese su contrasenia: ")

if contrasenia == "1234admin":
    print("Contrasenia valida, acceso permitido")
else:
    print("Contrasenia incorrecta, acceso denegado")