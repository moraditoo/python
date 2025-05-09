#Ejercicio #7: Cálculo de propina según satisfacción

monto = float(input("Ingrese el monto total: "))
                    
if monto < 0:
    print("Monto no valido")
    quit()
    
nivel_satisfaccion = input("¿Nivel de satisfacción (buena/mala)?: ").lower()

if nivel_satisfaccion == "buena":
        propina = monto * 0.15
elif nivel_satisfaccion == "mala":
        propina = monto * 0.05
else:
        print("Nivel de satisfacción inválido.")
        quit()

total = monto + propina

print(f"Total a pagar: C${total:.2f}")
    