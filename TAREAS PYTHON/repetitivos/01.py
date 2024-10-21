import os
os.system("cls")

def division_por_restas_sucesivas(dividendo, divisor):
    if divisor == 0:
        return None, None  # No se puede dividir entre cero

    cociente = 0
    resto = dividendo

    # Realiza la resta sucesiva
    while resto >= divisor:
        resto -= divisor
        cociente += 1

    return cociente, resto

# Solicitar entrada de usuario
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

# Calcular cociente y resto
cociente, resto = division_por_restas_sucesivas(dividendo, divisor)

# Mostrar resultado
if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"Cociente: {cociente}, Resto: {resto}")
