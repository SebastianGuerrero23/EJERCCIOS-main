import os
os.system("cls")

def calcular_precio(codigo, cantidad):
    # Definir precios unitarios
    precios = {
        101: 17,
        102: 25,
        103: 16,
        104: 27
    }

    # Verificar si el código es válido
    if codigo in precios:
        precio_unitario = precios[codigo]
        importe_compra = precio_unitario * cantidad
        
        # Calcular el descuento según la cantidad de unidades
        if 1 <= cantidad <= 10:
            descuento = 0.05  # 5%
        elif 11 <= cantidad <= 20:
            descuento = 0.08  # 8%
        elif 21 <= cantidad <= 30:
            descuento = 0.10  # 10%
        else:
            descuento = 0.13  # 13%

        monto_descuento = importe_compra * descuento
        total_pagar = importe_compra - monto_descuento
        return importe_compra, monto_descuento, total_pagar
    else:
        return None, None, None

# Ejemplo de uso
codigo_producto = 102  # Cambia el código del producto
cantidad_producto = 15  # Cambia la cantidad según sea necesario

importe, descuento, total = calcular_precio(codigo_producto, cantidad_producto)

if importe is not None:
    print(f"Importe de la compra: {importe}")
    print(f"Descuento aplicado: {descuento}")
    print(f"Total a pagar: {total}")
else:
    print("Código de producto no válido.")