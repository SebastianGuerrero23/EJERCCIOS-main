import os
os.system("cls")

def calcular_lapiceros(cuadernos):
    if cuadernos < 12:
        return 0, 0, 0  # (Lucas, Faber, Pilot)
    elif 12 <= cuadernos < 24:
        lapiceros_lucas = cuadernos // 4
        return lapiceros_lucas, 0, 0
    elif 24 <= cuadernos < 36:
        lapiceros_faber = 2 * (cuadernos // 4)
        return 0, lapiceros_faber, 0
    else:  # cuadernos >= 36
        lapiceros_pilot = 2 * (cuadernos // 4)
        lapiceros_faber = cuadernos // 6
        lapiceros_lucas = cuadernos // 12
        return lapiceros_lucas, lapiceros_faber, lapiceros_pilot

# Ejemplo de uso
cuadernos = int(input("Ingrese el número de cuadernos adquiridos: "))  # Número de cuadernos

lapiceros_lucas, lapiceros_faber, lapiceros_pilot = calcular_lapiceros(cuadernos)

print(f"Lapiceros Lucas obsequiados: {lapiceros_lucas}")
print(f"Lapiceros Faber obsequiados: {lapiceros_faber}")
print(f"Lapiceros Pilot obsequiados: {lapiceros_pilot}")
