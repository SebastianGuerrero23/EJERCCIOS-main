import os
os.system("cls")

def permutaciones(cadena):
    if len(cadena) == 0:
        return ['']
    
    resultado = []
    for i in range(len(cadena)):
        letra = cadena[i]
        subcadena = cadena[:i] + cadena[i+1:]
        for perm in permutaciones(subcadena):
            resultado.append(letra + perm)
    
    return resultado

print(permutaciones("abc"))
