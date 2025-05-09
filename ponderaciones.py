#7. Calcula la calificación final de un estudiante con ponderaciones: Tareas: 30% Examen parcial: 30% Examen final: 40%
tarea = 0.3*100
examen_parcial = 0.3*100
examen_final = 0.4*100
total = tarea+examen_parcial+examen_final
tarea1 = float(input("Cuanto puntaje saco en la tarea? "))
examen_parcial1= float(input("Cuanto puntaje saco en el examen parcial? "))
examen_final1 = float(input("Cuanto puntaje saco en el examen final? "))
cal1 = tarea1*tarea
cal2 = examen_parcial1*examen_parcial
cal3 = examen_final1*examen_final
calificacion_final = (cal1+cal2+cal3)/100
print("Su calilificacion final es de: ",calificacion_final)
