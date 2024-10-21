import os
os.system("cls")

def tipo_empleado(codigo):
    if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0:
        return "Administrativo"
    elif codigo % 3 == 0 and codigo % 5 == 0:
        return "Directivo"
    elif codigo % 2 == 0:
        return "Vendedor"
    else:
        return "Seguridad"

# Ejemplo de uso
codigo = int(input("Ingrese el código del empleado (tres cifras): "))  # Código entero de tres cifras

# Verificar que el código sea de tres cifras
if 100 <= codigo <= 999:
    tipo = tipo_empleado(codigo)
    print(f"El tipo de empleado es: {tipo}")
else:
    print("El código debe ser un número entero de tres cifras.")
