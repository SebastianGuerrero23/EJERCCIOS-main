import os
os.system("cls")

def contar_ocurrencias(lista, elemento):
    return sum(1 for x in lista if x == elemento)

print(contar_ocurrencias([1, 2, 3, 1, 4, 1], 1))