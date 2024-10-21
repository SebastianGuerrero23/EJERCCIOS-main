import os
os.system("cls")

def calcular_bonificacion(sueldo_bruto, num_hijos):
    if num_hijos > 1:
        bonificacion = (sueldo_bruto * 0.125) + (num_hijos * 40)  # 12.5% del sueldo + S/. 40 por cada hijo
    else:
        bonificacion = sueldo_bruto * 0.10  # 10% del sueldo
    
    # Calcular el sueldo neto a pagar
    sueldo_neto = sueldo_bruto + bonificacion
    
    return bonificacion, sueldo_neto

# Ejemplo de uso
sueldo_bruto = 2000  # Cambia este valor según el sueldo bruto del empleado
num_hijos = 3       # Cambia este valor según el número de hijos del empleado

bonificacion, sueldo_neto = calcular_bonificacion(sueldo_bruto, num_hijos)

print(f"Bonificación: S/. {bonificacion:.2f}")
print(f"Sueldo neto a pagar: S/. {sueldo_neto:.2f}")
