import os
os.system("cls")

# Ingreso del número de 4 cifras
numero = input("Ingrese un número de 4 cifras: ")

# Verificar que el número tenga exactamente 4 cifras
if len(numero) != 4 or not numero.isdigit():
    print("Por favor, ingrese un número válido de 4 cifras.")


else:
    # Extraer las cifras y convertirlas a una lista de enteros
    cifras = [int(d) for d in numero]

    # Encontrar la mayor y menor cifra
    mayor_cifra = max(cifras)
    menor_cifra = min(cifras)

    # Formar el mayor número posible de dos cifras
    mayor_numero = mayor_cifra * 10 + menor_cifra

    # Mostrar el resultado
    print(f"El mayor número posible de dos cifras es: {mayor_numero}")