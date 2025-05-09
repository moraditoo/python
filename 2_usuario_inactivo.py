#Ejercicio#2. Detectar si un usuario está inactivo por más de 30 días

from datetime import datetime

#Ingresar fecha del último inicio de sesión
fecha_ultimo_inicio = input("Ingrese la fecha de último inicio de sesión (YYYY-MM-DD): ")

#Convertir la entrada a un objeto de fecha
fecha_ultimo_inicio = datetime.strptime(fecha_ultimo_inicio, "%Y-%m-%d").date()

#Obtener la fecha actual
fecha_actual = datetime.now().date()

#Calcular días transcurridos
dias_transcurridos = (fecha_actual - fecha_ultimo_inicio).days

#Evaluar si han pasado más de 30 días
if dias_transcurridos > 30:
    print("Cuenta inactiva")
else:
    print("Cuenta activa")