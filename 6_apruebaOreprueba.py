#6 Evaluar si un estudiante aprueba o reprueba

calificacion = float(input("Ingrese la calificacion: "))

if calificacion < 0:
    print("Numero no valido")
    quit()
elif calificacion >= 101:
    print("Numero no valido")
    quit()
elif calificacion >= 70:
    print("Aprobado")
    quit()
elif calificacion < 70:
    print("Reprobado")
    quit()
