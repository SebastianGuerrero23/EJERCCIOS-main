import os
os.system("cls")

def calcular_sueldo(horas_trabajadas, categoria):
    # Definir la tarifa por hora según la categoría
    tarifas = {
        'A': 21.00,
        'B': 19.50,
        'C': 17.00,
        'D': 15.50
    }
    
    # Verificar si la categoría es válida
    if categoria not in tarifas:
        return "Error: Categoría inválida."

    # Calcular sueldo bruto
    tarifa_hora = tarifas[categoria]
    sueldo_bruto = horas_trabajadas * tarifa_hora
    
    # Calcular el porcentaje de descuento
    if sueldo_bruto > 2500:
        descuento = sueldo_bruto * 0.20  # 20% de descuento
    else:
        descuento = sueldo_bruto * 0.15  # 15% de descuento
    
    # Calcular sueldo neto
    sueldo_neto = sueldo_bruto - descuento
    
    return sueldo_bruto, descuento, sueldo_neto

# Ejemplo de uso
horas_trabajadas = 130  # Cambia este valor según las horas trabajadas
categoria = 'B'         # Cambia este valor a 'A', 'B', 'C' o 'D' según la categoría

resultado = calcular_sueldo(horas_trabajadas, categoria)

if isinstance(resultado, str):
    print(resultado)  # Imprimir mensaje de error
else:
    sueldo_bruto, descuento, sueldo_neto = resultado
    print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
    print(f"Descuento: S/. {descuento:.2f}")
    print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
