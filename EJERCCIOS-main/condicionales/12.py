import os
os.system("cls")

def determinar_dia(numero):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias_semana[numero - 1] * (1 <= numero <= 7)

# Ejemplo 
numero_dia = 3  # Numero de las semana seguno 1 a 7

dia = determinar_dia(numero_dia)
if dia:
    print(f"El día correspondiente es: {dia}")
else:
    print("Número fuera de rango. Debe ser entre 1 y 7.")