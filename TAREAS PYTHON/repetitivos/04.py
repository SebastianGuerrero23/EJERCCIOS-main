import os
os.system("cls")

def mostrar_multiplos(n, m):
    multiplos = []
    for i in range(1, m + 1):
        multiplos.append(n * i)  # Calcula el múltiplo
    return multiplos

# Solicitar entrada de usuario
n = int(input("Ingrese un número (n): "))
m = int(input("Ingrese la cantidad de múltiplos a mostrar (m): "))

# Obtener los múltiplos
multiplos = mostrar_multiplos(n, m)

# Mostrar resultados
print(f"Los {m} múltiplos de {n} son: {', '.join(map(str, multiplos))}")
