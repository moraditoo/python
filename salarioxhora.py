nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))
sueldo_bruto = horas_trabajadas * precio_por_hora
descuento = sueldo_bruto * 0.05
sueldo_neto = sueldo_bruto - descuento
# Mostramos los resultados
print("Nombre del trabajador:", nombre)
print("Sueldo bruto: C${:.2f}".format(sueldo_bruto))
print("Descuento por renta (5%): C${:.2f}".format(descuento))
print("Salario neto a pagar: C${:.2f}".format(sueldo_neto))