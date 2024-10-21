import os
os.system("cls")
import random

def contar_ocurrencias(lista, elemento):
    return lista.count(elemento)

def sumar_lista(lista):
    return sum(lista)

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

# Uso del programa
cadena = "abc"
conjunto = ['a', 'b', 'c']
numeros = [random.randint(1, 100) for _ in range(10)]

print("Permutaciones de 'abc':", permutaciones(cadena))
print("Combinaciones de ['a', 'b', 'c'] tomando 2:", combinaciones(conjunto, 2))
print("Lista aleatoria:", numeros)
print("Suma de la lista:", sumar_lista(numeros))
print("Ocurrencias del número 1 en la lista:", contar_ocurrencias(numeros, 1))
