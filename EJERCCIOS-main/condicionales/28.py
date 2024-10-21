import os
os.system("cls")

def calcular_sueldo(monto_vendido):
    sueldo_basico = 600  # Sueldo básico
    comision = monto_vendido * 0.15  # Comisión del 15%
    
    # Calcular sueldo bruto
    sueldo_bruto = sueldo_basico + comision
    
    # Determinar el porcentaje de descuento
    if sueldo_bruto > 1800:
        descuento = sueldo_bruto * 0.10  # 10% de descuento
    else:
        descuento = sueldo_bruto * 0.05  # 5% de descuento
    
    # Calcular sueldo neto
    sueldo_neto = sueldo_bruto - descuento
    
    # Determinar el número de polos obsequiados
    if monto_vendido > 1000:
        polos = 3  # 3 polos si se vende más de S/. 1000
    else:
        polos = 1  # 1 polo en caso contrario
    
    return sueldo_bruto, descuento, sueldo_neto, polos

# Ejemplo de uso
monto_vendido = 1200  # Cambia este valor según el monto total vendido

sueldo_bruto, descuento, sueldo_neto, polos = calcular_sueldo(monto_vendido)

print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
print(f"Número de polos obsequiados: {polos}")
