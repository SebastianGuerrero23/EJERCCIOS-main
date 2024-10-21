import os
os.system("cls")

def calcular_compra(cantidad_docenas, precio_por_docena):
    # Calcular el monto de la compra
    monto_compra = cantidad_docenas * precio_por_docena
    
    # Determinar el descuento
    if cantidad_docenas >= 6:
        descuento = monto_compra * 0.15  # 15% de descuento
    else:
        descuento = monto_compra * 0.10  # 10% de descuento

    # Calcular el total a pagar
    total_a_pagar = monto_compra - descuento
    
    # Determinar la cantidad de lapiceros de obsequio
    if cantidad_docenas >= 30:
        lapiceros_obsequio = (cantidad_docenas // 3) * 2  
    else:
        lapiceros_obsequio = 0  
    
    return monto_compra, descuento, total_a_pagar, lapiceros_obsequio

# Ejemplo 
cantidad_docenas = 35  
precio_por_docena = 50  

monto_compra, descuento, total_a_pagar, lapiceros_obsequio = calcular_compra(cantidad_docenas, precio_por_docena)

print(f"Monto de la compra: S/. {monto_compra:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")
print(f"Cantidad de lapiceros de obsequio: {lapiceros_obsequio}")