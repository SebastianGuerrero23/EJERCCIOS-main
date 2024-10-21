import os
os.system("cls")

def suma_cifras_pares_impares(numero):
    suma_pares = 0
    suma_impares = 0

    # Separar las cifras y calcular las sumas
    for cifra in str(numero):
        if int(cifra) % 2 == 0:  # Cifra par
            suma_pares += int(cifra)
        else:  # Cifra impar
            suma_impares += int(cifra)

    return suma_pares, suma_impares

def encontrar_numeros():
    numeros_encontrados = []

    # Iterar sobre todos los números de 4 cifras
    for numero in range(1000, 10000):
        suma_pares, suma_impares = suma_cifras_pares_impares(numero)
        if suma_pares == suma_impares:
            numeros_encontrados.append(numero)

    return numeros_encontrados

# Ejecutar el programa
numeros = encontrar_numeros()
cantidad = len(numeros)

# Mostrar resultados
print("Números de 4 cifras con suma de cifras pares igual a la suma de cifras impares:")
for numero in numeros:
    print(numero)
print(f"\nCantidad de números encontrados: {cantidad}")
