import os
os.system("cls")

def mostrar_rectangulo(n):
    for _ in range(n):
        print('*' * (2 * n))

# Solicitar entrada de usuario
n = int(input("Ingrese la altura del rectángulo (n) (debe ser >= 4): "))

# Verificar que n sea mayor o igual a 4
if n >= 4:
    mostrar_rectangulo(n)
else:
    print("El valor de n debe ser mayor o igual a 4.")
