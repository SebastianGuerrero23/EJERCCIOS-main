import os
os.system("cls")

# Propina base
propina_base = 20
# Monto adicional por examen aprobado
propina_por_examen = 5

# Ingreso de la cantidad de exámenes aprobados
examenes_aprobados = int(input("Ingrese la cantidad de exámenes aprobados (0 a 3): "))

# Verificar que el número de exámenes aprobados esté dentro del rango permitido
if examenes_aprobados < 0 or examenes_aprobados > 3:
    print("Por favor, ingrese un número válido de exámenes aprobados (0 a 3).")

else:
    # Calcular la propina total
    propina_total = propina_base + (examenes_aprobados * propina_por_examen)

    # Mostrar el resultado
    print(f"El monto total de la propina es: S/. {propina_total}")