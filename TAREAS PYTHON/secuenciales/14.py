import os, math
os.system("cls")

numeros = []

for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

numeros.sort(reverse=True)

promedio = (numeros[0] + numeros[1] + numeros[2]) / 3

print(f"El promedio de los 3 números mayores es: {promedio:.2f}")
