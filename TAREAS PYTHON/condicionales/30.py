import os
os.system("cls")

def calcular_pago(cuota, dias):
    # Verificar el período de pago y calcular el monto a pagar
    if dias <= 10:
        # Descuento para pago dentro de los primeros 10 días
        descuento = max(5, cuota * 0.02)
        total_a_pagar = cuota - descuento
    elif dias <= 20:
        # No hay descuento ni recargo para pago en los siguientes 10 días
        total_a_pagar = cuota
    else:
        # Recargo para pago dentro de los últimos días del mes
        recargo = max(10, cuota * 0.03)
        total_a_pagar = cuota + recargo
    
    return total_a_pagar

# Ejemplo de uso
cuota = 100  # Cambia este valor según la cuota mensual
dias = 12    # Cambia este valor según el día en que se realiza el pago

total_a_pagar = calcular_pago(cuota, dias)

print(f"Total a pagar: S/. {total_a_pagar:.2f}")
