salario_bruto = float(input("Ingrese el salario actual del empleado: "))
salario_nuevo = salario_bruto*1.08
descuento_salario = (salario_nuevo*0.025)
salario_neto = salario_nuevo-descuento_salario
print("Se le desconto 2,5% por servicios:", descuento_salario)
print("El nuevo salario es: ", salario_neto)
