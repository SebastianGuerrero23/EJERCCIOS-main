import os
os.system("cls")

def calcular_pension(categoria, promedio):
    # Definir la pensión y el descuento según la categoría y el promedio
    pensiones = {
        'A': 550,
        'B': 500,
        'C': 450,
        'D': 400
    }

    descuentos = {
        'B': (0.10, 14, 15.99),  # 10% descuento
        'C': (0.12, 16, 17.99),  # 12% descuento
        'D': (0.15, 18, 20)       # 15% descuento
    }
    
    # Verificar si la categoría es válida
    if categoria not in pensiones:
        return "Error: Categoría inválida."
    
    # Obtener la pensión actual
    pension_actual = pensiones[categoria]

    # Determinar si hay descuento
    if categoria in descuentos:
        porcentaje_descuento, rango_inferior, rango_superior = descuentos[categoria]
        if rango_inferior <= promedio <= rango_superior:
            descuento = pension_actual * porcentaje_descuento
        else:
            descuento = 0
    else:
        descuento = 0

    # Calcular nueva pensión
    nueva_pension = pension_actual - descuento

    return pension_actual, descuento, nueva_pension

# Ejemplo de uso
categoria = 'C'        # Cambia este valor a 'A', 'B', 'C' o 'D' según la categoría
promedio = 17          # Cambia este valor según el promedio ponderado del ciclo anterior

resultado = calcular_pension(categoria, promedio)

if isinstance(resultado, str):
    print(resultado)  # Imprimir mensaje de error
else:
    pension_actual, descuento, nueva_pension = resultado
    print(f"Pensión actual: S/. {pension_actual:.2f}")
    print(f"Descuento: S/. {descuento:.2f}")
    print(f"Nueva pensión: S/. {nueva_pension:.2f}")
