import os
os.system("cls")

def calcular_imc(peso, estatura):
    # Calcular el IMC
    imc = peso / (estatura ** 2)
    return imc

def grado_obesidad(imc):
    # Determinar el grado de obesidad
    if imc < 20:
        return "Delgado"
    elif 20 <= imc <= 25:
        return "Normal"
    elif 25 < imc <= 27:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Ejemplo de uso
peso = float(input("Ingrese el peso en kg: "))  # Peso en kilogramos
estatura = float(input("Ingrese la estatura en metros: "))  # Estatura en metros

imc_resultado = calcular_imc(peso, estatura)
grado = grado_obesidad(imc_resultado)

print(f"El IMC es: {imc_resultado:.2f}")
print(f"Grado de Obesidad: {grado}")
