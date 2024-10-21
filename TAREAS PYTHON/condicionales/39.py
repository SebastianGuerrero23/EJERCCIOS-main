import os
os.system("cls")

def grado_eficiencia(ausencias, tornillos_defectuosos, tornillos_no_defectuosos):
    # Inicializa las condiciones
    cumple_condicion1 = ausencias <= 1.5
    cumple_condicion2 = tornillos_defectuosos < 300
    cumple_condicion3 = tornillos_no_defectuosos > 10000
    
    # Determina el grado de eficiencia
    if cumple_condicion1 and cumple_condicion2 and cumple_condicion3:
        return 20
    elif cumple_condicion1 and cumple_condicion2:
        return 12
    elif cumple_condicion1 and cumple_condicion3:
        return 13
    elif cumple_condicion2 and cumple_condicion3:
        return 15
    elif cumple_condicion1:
        return 7
    elif cumple_condicion2:
        return 8
    elif cumple_condicion3:
        return 9
    else:
        return 5

# Solicitar entrada de usuario
ausencias = float(input("Ingrese el número de horas de ausencia: "))
tornillos_defectuosos = int(input("Ingrese la cantidad de tornillos defectuosos producidos: "))
tornillos_no_defectuosos = int(input("Ingrese la cantidad de tornillos no defectuosos producidos: "))

# Calcular el grado de eficiencia
grado = grado_eficiencia(ausencias, tornillos_defectuosos, tornillos_no_defectuosos)

# Mostrar resultado
print(f"El grado de eficiencia del operario es: {grado}")
