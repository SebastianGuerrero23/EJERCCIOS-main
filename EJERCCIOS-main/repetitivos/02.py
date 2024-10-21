import os
os.system("cls")

def multiplicar(num1, num2):
    # Si uno de los números es 0, el resultado es 0
    if num1 == 0 or num2 == 0:
        return 0
    
    resultado = 0
    # Utilizar sumas sucesivas
    for _ in range(abs(num2)):
        resultado += abs(num1)

    # Ajustar el signo del resultado
    if (num1 < 0) ^ (num2 < 0):  # XOR para determinar el signo
        resultado = -resultado

    return resultado

# Solicitar entrada de usuario
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Calcular el producto
producto = multiplicar(num1, num2)

# Mostrar resultado
print(f"El producto de {num1} y {num2} es: {producto}")
