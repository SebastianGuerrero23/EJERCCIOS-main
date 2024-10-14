import os
os.system("cls")

unidades = int( input("Unidades :") )
precio = float( input("Precio :") )

compra = unidades * precio
descuento_1 = 0.15 * compra
descuento_2 = 0.15 * ( compra - descuento_1 )
descuento = descuento_1 + descuento_2

print(f"Compra = {compra:.2f}")
print(f"Descuento = {descuento:.2f}")
print(f"Total : {(compra - descuento):.2f}")

