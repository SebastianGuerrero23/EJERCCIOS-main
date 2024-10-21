import os
os.system("cls")

def filtrar_mayores(lista, umbral):
    return [x for x in lista if x > umbral]

print(filtrar_mayores([1, 2, 3, 4, 5], 3))
