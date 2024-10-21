import os
os.system("cls")

def contar_divisores(numero):
    contador = 0
    # Iterar desde 1 hasta el número
    for i in range(1, abs(numero) + 1):
        if numero % i == 0:  # Verifica si i es un divisor
            contador += 1
    return contador

# Solicitar entrada de usuario
numero = int(input("Ingrese un número entero: "))

# Calcular la cantidad de divisores
cantidad_divisores = contar_divisores(numero)

# Mostrar resultado
print(f"La cantidad de divisores de {numero} es: {cantidad_divisores}")
