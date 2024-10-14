import os
os.system("cls")

# Ingreso de los tres números
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Determinar el número intermedio
# Sumar todos y restar el mayor y el menor
suma = num1 + num2 + num3
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
intermedio = suma - mayor - menor

# Mostrar el resultado
print(f"El número intermedio es: {intermedio}")