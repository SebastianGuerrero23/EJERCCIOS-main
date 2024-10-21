import os
os.system("cls")

def calcular_compra(unidades_a, unidades_b):
    precio_a = 25  # Precio por unidad del producto A
    precio_b = 30  # Precio por unidad del producto B
    
    # Calcular el importe bruto
    importe_a = unidades_a * precio_a
    importe_b = unidades_b * precio_b
    importe_bruto = importe_a + importe_b
    
    # Calcular el descuento
    if unidades_a > 50:
        descuento_a = importe_a * 0.15  # 15% de descuento en producto A
    else:
        descuento_a = 0
    
    if unidades_b > 60:
        descuento_b = importe_b * 0.10  # 10% de descuento en producto B
    else:
        descuento_b = 0
    
    # Total descuento
    total_descuento = descuento_a + descuento_b
    
    # Calcular total a pagar
    total_a_pagar = importe_bruto - total_descuento
    
    return importe_bruto, total_descuento, total_a_pagar

# Ejemplo de uso
unidades_producto_a = 60  # Cambia este valor según la cantidad de unidades del producto A
unidades_producto_b = 70  # Cambia este valor según la cantidad de unidades del producto B

importe_bruto, descuento, total_a_pagar = calcular_compra(unidades_producto_a, unidades_producto_b)

print(f"Importe bruto: S/. {importe_bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total_a_pagar:.2f}")
