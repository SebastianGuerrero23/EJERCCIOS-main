import os
os.system("cls")

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    meses = {
        1: ("Enero", 31),
        2: ("Febrero", 28),  # Se ajusta si es bisiesto más adelante
        3: ("Marzo", 31),
        4: ("Abril", 30),
        5: ("Mayo", 31),
        6: ("Junio", 30),
        7: ("Julio", 31),
        8: ("Agosto", 31),
        9: ("Septiembre", 30),
        10: ("Octubre", 31),
        11: ("Noviembre", 30),
        12: ("Diciembre", 31)
    }

    if mes < 1 or mes > 12:
        return "Mes inválido."

    nombre_mes, dias = meses[mes]

    # Ajustar días si el mes es febrero y el año es bisiesto
    if mes == 2 and es_bisiesto(anio):
        dias = 29

    return nombre_mes, dias

# Solicitar entrada de usuario
mes = int(input("Ingrese el número del mes (1-12): "))
anio = int(input("Ingrese el año: "))

# Obtener resultado
nombre_mes, cantidad_dias = dias_en_mes(mes, anio)

# Mostrar resultado
print(f"El mes de {nombre_mes} tiene {cantidad_dias} días.")