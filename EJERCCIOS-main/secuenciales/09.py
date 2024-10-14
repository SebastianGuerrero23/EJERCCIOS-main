import os
os.system("cls")

numero = int( input("Ingrese un número de 4 cifras: ") )

# Convertir el número en una cadena y sumar cada dígito
cifra_1 = int(str(numero)[0])
cifra_2 = int(str(numero)[1])
cifra_3 = int(str(numero)[2])
cifra_4 = int(str(numero)[3])

suma = cifra_1 + cifra_2 + cifra_3 + cifra_4

print(f"Suma de las cifras = {suma}")