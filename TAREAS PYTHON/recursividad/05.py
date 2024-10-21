import os
os.system("cls")

def contar_ocurrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

print(contar_ocurrencias([1, 2, 3, 1, 4, 1], 1))