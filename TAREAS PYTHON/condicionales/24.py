import os
os.system("cls")

def calcular_sueldo(monto_vendido):
    # Calcular el sueldo base como el 10% del monto vendido
    sueldo_base = monto_vendido * 0.10
    
    # Calcular el exceso sobre S/. 5000
    if monto_vendido > 5000:
        exceso = monto_vendido - 5000
        # Calcular el adicional por cada S/. 500 de exceso
        adicional = (exceso // 500) * 25  # S/. 25 por cada S/. 500 de exceso
    else:
        adicional = 0  # No hay exceso, no hay adicional
    
    # Calcular el sueldo total
    sueldo_total = sueldo_base + adicional
    
    return sueldo_total

# Ejemplo de uso
monto_vendido = 6000  # Cambia este valor según el monto total vendido

sueldo = calcular_sueldo(monto_vendido)

print(f"Sueldo del vendedor: S/. {sueldo:.2f}")
