import os
os.system("cls")

sueldo_basico = 500  # Sueldo básico mensual

monto_vendido = float(input ("Ingrese el monto total vendido: ") )

comision = monto_vendido * 0.09  # 9% del monto vendido
sueldo_bruto = sueldo_basico + comision  # Sueldo bruto
descuento = sueldo_bruto * 0.11  # 11% de descuento
sueldo_neto = sueldo_bruto - descuento  # Sueldo neto

print(f"Comisión: S/. {comision:.2f}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")

