import os
os.system("cls")

def determinar_orden(a, b, c):
    if a < b < c:
        return "Los números están en orden ascendente."
    elif a > b > c:
        return "Los números están en orden descendente."
    else:
        return "Los números están en desorden."

# Ejemplo de uso
a = 5  # Cambia este valor según sea necesario
b = 3  # Cambia este valor según sea necesario
c = 1  # Cambia este valor según sea necesario

resultado = determinar_orden(a, b, c)
print(resultado)