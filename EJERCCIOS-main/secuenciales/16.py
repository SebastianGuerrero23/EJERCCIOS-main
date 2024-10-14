import os
os.system("cls")

horas_trabajadas = float(input("Ingrese el número total de horas trabajadas: "))
tarifa_horaria = float(input("Ingrese la tarifa horaria: "))

sueldo_basico = horas_trabajadas * tarifa_horaria

bonificacion = sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion

descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print (f"Sueldo básico: S/. {sueldo_basico:.2f}" )
print (f"Sueldo bruto: S/. {sueldo_bruto:.2f}" )
print (f"Sueldo neto: S/. {sueldo_neto:.2f}" )