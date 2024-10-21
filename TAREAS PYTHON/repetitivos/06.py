import os
os.system("cls")

def tabla_multiplicar(n, x, y):
    print(f"Tabla de multiplicar del {n} del {x} al {y}:")
    for i in range(x, y + 1):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

# Solicitar entrada de usuario
n = int(input("Ingrese un número para generar su tabla de multiplicar: "))
x = int(input("Ingrese el valor inicial (x) de la tabla: "))
y = int(input("Ingrese el valor final (y) de la tabla: "))

# Mostrar la tabla de multiplicar
tabla_multiplicar(n, x, y)
