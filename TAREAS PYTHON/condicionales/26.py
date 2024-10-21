import os
os.system("cls")

def calcular_pago(monto_compra):
    # Determinar el porcentaje de préstamo y la cantidad a pedir prestada
    if monto_compra > 5000:
        porcentaje_prestamo = 0.30  # 30%
    else:
        porcentaje_prestamo = 0.20  # 20%
    
    monto_prestado = monto_compra * porcentaje_prestamo
    interes = monto_prestado * 0.10  # 10% de interés
    total_prestamo = monto_prestado + interes  # Total a pagar al banco
    
    # Calcular cuánto cubrirá la empresa con su propio dinero
    dinero_propio = monto_compra - monto_prestado
    
    return dinero_propio, total_prestamo

# Ejemplo de uso
monto_compra = 6000  # Cambia este valor según el monto total de la compra

dinero_propio, total_prestamo = calcular_pago(monto_compra)

print(f"Dinero que cubrirá la empresa: S/. {dinero_propio:.2f}")
print(f"Total a pagar al banco (incluyendo intereses): S/. {total_prestamo:.2f}")
