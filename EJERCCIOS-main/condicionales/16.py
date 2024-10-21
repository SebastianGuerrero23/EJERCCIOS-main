import os
os.system("cls")

def calcular_cuotas(costo_casa, ingreso_mensual):
    if ingreso_mensual < 1250:
        cuota_inicial = costo_casa * 0.15  # 15% del costo de la casa
        cuotas_mensuales = 120  
    else:
        cuota_inicial = costo_casa * 0.30  # 30% del costo de la casa
        cuotas_mensuales = 75  

    monto_prestamo = costo_casa - cuota_inicial
    cuota_mensual = monto_prestamo / cuotas_mensuales
    
    return cuota_inicial, cuota_mensual

# Ejemplo 
costo_casa = 100000  
ingreso_mensual = 1300  

cuota_inicial, cuota_mensual = calcular_cuotas(costo_casa, ingreso_mensual)

print(f"Cuota inicial: S/. {cuota_inicial:.2f}")
print(f"Monto de la cuota mensual: S/. {cuota_mensual:.2f}")
