import os
os.system("cls")

def calcular_promedio(notas):
    # Se ordena de menor a mayor
    notas_ordenadas = sorted(notas)
    
    # Elimina la nota más baja y la más alta
    nota_menor = notas_ordenadas.pop(0)
    nota_mayor = notas_ordenadas.pop(-1)
    
    # Calcula el promedio de las notas restantes
    promedio = sum(notas_ordenadas) / len(notas_ordenadas)
    
    return nota_menor, nota_mayor, promedio

# Ejemplo
notas = [15, 12, 18, 10, 20] 

nota_eliminada_menor, nota_eliminada_mayor, promedio_aprobatorio = calcular_promedio(notas)

print(f"Nota eliminada (menor): {nota_eliminada_menor}")
print(f"Nota eliminada (mayor): {nota_eliminada_mayor}")
print(f"Promedio aprobatorio: {promedio_aprobatorio:.2f}")