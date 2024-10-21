import os
os.system("cls")

def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

# Solicitar entrada de usuario
n = int(input("Ingrese la base (n): "))
m = int(input("Ingrese el exponente (m): "))

# Calcular y mostrar la potencia
resultado = potencia(n, m)
print(f"{n} elevado a {m} es: {resultado}")
