import os
os.system("cls")

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Solicitar entrada de usuario
n = int(input("Ingrese un número para calcular su factorial: "))

# Calcular y mostrar el factorial
resultado = calcular_factorial(n)
print(f"El factorial de {n} es: {resultado}")
