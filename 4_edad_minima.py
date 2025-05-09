#Ejercicio#4. Validar edad mínima para votar

edad = int(input("Ingrese su edad: "))

if edad <= 0:
    print("Edad no valida")
    quit()
    
if edad >= 18:
    print("Puede votar")
else:
    print("Usted no puede votar")
