import os
os.system("cls")

def calcular_bonificacion(minutos_tardanza, observaciones):
    # Calcular puntaje por puntualidad
    if minutos_tardanza == 0:
        puntaje_puntualidad = 10
    elif 1 <= minutos_tardanza <= 2:
        puntaje_puntualidad = 8
    elif 3 <= minutos_tardanza <= 5:
        puntaje_puntualidad = 6
    elif 6 <= minutos_tardanza <= 9:
        puntaje_puntualidad = 4
    else:  # Más de 9 minutos
        puntaje_puntualidad = 0

    # Calcular puntaje por rendimiento
    if observaciones == 0:
        puntaje_rendimiento = 10
    elif observaciones == 1:
        puntaje_rendimiento = 8
    elif observaciones == 2:
        puntaje_rendimiento = 5
    elif observaciones == 3:
        puntaje_rendimiento = 1
    else:  # Más de 3 observaciones
        puntaje_rendimiento = 0

    # Calcular puntaje total
    puntaje_total = puntaje_puntualidad + puntaje_rendimiento

    # Determinar bonificación
    if puntaje_total == 20:
        bonificacion = puntaje_total * 12.5
    elif 17 <= puntaje_total <= 19:
        bonificacion = puntaje_total * 10.0
    elif 14 <= puntaje_total <= 16:
        bonificacion = puntaje_total * 7.5
    elif 11 <= puntaje_total <= 13:
        bonificacion = puntaje_total * 5.0
    else:  # Puntaje total menor a 11
        bonificacion = puntaje_total * 2.5

    return puntaje_puntualidad, puntaje_rendimiento, puntaje_total, bonificacion

# Ejemplo de uso
minutos_tardanza = 4  # Cambia este valor según los minutos de tardanza
observaciones = 1      # Cambia este valor según la cantidad de observaciones

resultado = calcular_bonificacion(minutos_tardanza, observaciones)

puntaje_puntualidad, puntaje_rendimiento, puntaje_total, bonificacion = resultado

print(f"Puntaje por puntualidad: {puntaje_puntualidad}")
print(f"Puntaje por rendimiento: {puntaje_rendimiento}")
print(f"Puntaje total: {puntaje_total}")
print(f"Bonificación anual: S/. {bonificacion:.2f}")
