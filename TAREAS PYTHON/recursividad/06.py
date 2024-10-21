import os
os.system("cls")

def contar_ocurrencias(lista, elemento):
    return len(list(filter(lambda x: x == elemento, lista)))

print(contar_ocurrencias([1, 2, 3, 1, 4, 1], 1))
