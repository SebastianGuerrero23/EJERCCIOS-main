import os
os.system("cls")

def calcular_descuento(numero_tarjeta, monto_compra):
    # Verificar si el número es par y no menor de 100
    if numero_tarjeta % 2 == 0 and numero_tarjeta >= 100:
        descuento = 0.15  
    else:
        descuento = 0.05  
    
    monto_descuento = monto_compra * descuento
    total_pagar = monto_compra - monto_descuento
    
    return numero_tarjeta, monto_compra, monto_descuento, total_pagar

# Ejemplo
numero_tarjeta = 120 
monto_compra = 500  

tarjeta, compra, descuento, total = calcular_descuento(numero_tarjeta, monto_compra)

print(f"Número de la tarjeta: {tarjeta}")
print(f"Monto de la compra: {compra}")
print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {total}")