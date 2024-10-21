import os
os.system("cls")

import random

def lista_aleatoria(n, limite):
    return [random.randint(1, limite) for _ in range(n)]

print(lista_aleatoria(5, 10))