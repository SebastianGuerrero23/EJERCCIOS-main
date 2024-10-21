import os
os.system("cls")

def clasificar_angulo(grados):
    if grados == 0:
        return "Nulo"
    elif 0 < grados < 90:
        return "Agudo"
    elif grados == 90:
        return "Recto"
    elif 90 < grados < 180:
        return "Obtuso"
    elif grados == 180:
        return "Llano"
    elif 180 < grados < 360:
        return "Cóncavo"
    elif grados == 360:
        return "Completo"
    else:
        return "Ángulo no válido"

# Ejemplo 
angulo = 120  #Cambia el valor segun que angulo sea

clasificacion = clasificar_angulo(angulo)
print(f"El ángulo es: {clasificacion}")