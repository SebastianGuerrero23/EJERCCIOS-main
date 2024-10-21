import os
os.system("cls")

# Entradas
cantidad = int( input("Ingrese la cantidad del dinero en soles") )

# Billetes y monedas
billetes_200 = cantidad // 200
cantidad %= 200

billetes_100 = cantidad // 100
cantidad %= 100

billetes_50 = cantidad // 50
cantidad  %= 50

billetes_20 = cantidad // 20
cantidad %= 20

billetes_10 = cantidad // 10
cantidad %= 10

monedas_5 = cantidad // 5
cantidad %= 5

monedas_2 = cantidad // 2
cantidad %= 2

monedas_1 = cantidad // 1

# Salida

print (f"Billetes de 200: {billetes_200}" )
print (f"Billetes de 100: {billetes_100}" )
print (f"Billetes de 50: {billetes_50}" )
print (f"Billetes de 20: {billetes_20}" )
print (f"Billetes de 10: {billetes_10}" )
print (f"Monedas de 5: {monedas_5}" )
print (f"Monedas de 2: {monedas_2}" )
print (f"Monedas de 1: {monedas_1}" )

