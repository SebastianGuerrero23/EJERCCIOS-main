import os
os.system("cls")

def combinaciones(conjunto, k):
    if k == 0:
        return [[]]
    if not conjunto:
        return []
    primero = conjunto[0]
    sin_primero = conjunto[1:]
    combinaciones_con_primero = combinaciones(sin_primero, k - 1)
    combinaciones_sin_primero = combinaciones(sin_primero, k)
    for c in combinaciones_con_primero:
        c.append(primero)
    return combinaciones_con_primero + combinaciones_sin_primero

print(combinaciones(['a', 'b', 'c'], 2))
