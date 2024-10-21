import os
os.system("cls")

def tabla_multiplicar(n):
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 13):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

# Solicitar entrada de usuario
n = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar
tabla_multiplicar(n)
