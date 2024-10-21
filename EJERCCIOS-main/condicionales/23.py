import os
os.system("cls")

def calcular_propina(nota_matematicas, nota_fisica):
    # Calcular la propina de Matemáticas
    if nota_matematicas > 17:
        propina_matematicas = 3
    else:
        propina_matematicas = nota_matematicas * 1  # S/. 1 por cada punto
    
    # Calcular la propina de Física
    if nota_fisica > 15:
        propina_fisica = 2
    else:
        propina_fisica = 0.50  # S/. 0.50 si la nota es 15 o menos
    
    # Calcular la propina total
    propina_total = propina_matematicas + propina_fisica
    
    # Calcular el promedio de las notas
    promedio = (nota_matematicas + nota_fisica) / 2
    
    # Determinar si le obsequiará un reloj
    if promedio > 16:
        reloj_obsequio = "Sí"
    else:
        reloj_obsequio = "No"
    
    return propina_total, promedio, reloj_obsequio

# Ejemplo de uso
nota_matematicas = 18  # Cambia este valor según la nota de Matemáticas
nota_fisica = 14       # Cambia este valor según la nota de Física

propina_total, promedio, reloj_obsequio = calcular_propina(nota_matematicas, nota_fisica)

print(f"Propina total: S/. {propina_total:.2f}")
print(f"Promedio de notas: {promedio:.2f}")
print(f"¿Obsequiará un reloj? {reloj_obsequio}")
