import os
os.system("cls")

def calcular_sueldo(monto_vendido):
    sueldo_basico = 250
    # Determinar la comisión según el monto vendido
    if monto_vendido <= 5000:
        comision = monto_vendido * 0.05
    elif monto_vendido <= 10000:
        comision = monto_vendido * 0.08
    elif monto_vendido <= 20000:
        comision = monto_vendido * 0.10
    else:
        comision = monto_vendido * 0.15

    sueldo_bruto = sueldo_basico + comision
    
    # Determinar el descuento según el sueldo bruto
    if sueldo_bruto > 3500:
        descuento = sueldo_bruto * 0.15
    else:
        descuento = sueldo_bruto * 0.08

    sueldo_neto = sueldo_bruto - descuento
    
    return sueldo_bruto, sueldo_neto, descuento, comision

# Ejemplo 
monto_vendido = 12000  

sueldo_bruto, sueldo_neto, descuento, comision = calcular_sueldo(monto_vendido)

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Comisión aplicada: S/. {comision:.2f}")
