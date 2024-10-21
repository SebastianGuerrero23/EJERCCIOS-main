import os
os.system("cls")

def calcular_sueldo(horas_trabajadas, tarifa_hora):
    # Definir las horas normales y el recargo para horas extras
    horas_normales = min(horas_trabajadas, 48)
    horas_extras = max(0, horas_trabajadas - 48)
    
    # Calcular el sueldo bruto
    sueldo_bruto = (horas_normales * tarifa_hora) + (horas_extras * tarifa_hora * 1.20)
    
    # Determinar el descuento si el sueldo bruto es mayor a S/. 1500
    if sueldo_bruto > 1500:
        descuento = sueldo_bruto * 0.11  # 11% de descuento
    else:
        descuento = 0
    
    # Calcular el total a pagar
    total_a_pagar = sueldo_bruto - descuento
    
    return horas_trabajadas, tarifa_hora, sueldo_bruto, descuento, total_a_pagar

# Ejemplo de uso
horas_trabajadas = 50  # Cambia este valor según las horas trabajadas
tarifa_hora = 30       # Cambia este valor según la tarifa por hora

horas_trabajadas, tarifa_hora, sueldo_bruto, descuento, total_a_pagar = calcular_sueldo(horas_trabajadas, tarifa_hora)

print(f"Horas trabajadas: {horas_trabajadas}")
print(f"Pago por hora: S/. {tarifa_hora:.2f}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")