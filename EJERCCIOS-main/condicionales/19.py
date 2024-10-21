import os
os.system("cls")

def categorizar_postulante(sexo, edad):
    if sexo.lower() == 'femenino':
        if edad < 23:
            categoria = 'FA'  # Femenino menor de 23
        else:
            categoria = 'FB'  # Femenino 23 o más
    elif sexo.lower() == 'masculino':
        if edad < 25:
            categoria = 'MA'  # Masculino menor de 25
        else:
            categoria = 'MB'  # Masculino 25 o más
    else:
        categoria = 'Categoría no válida'  # Si el sexo no es reconocido
    
    return categoria

# Ejemplo 
sexo_postulante = 'femenino'  
edad_postulante = 22  

categoria = categorizar_postulante(sexo_postulante, edad_postulante)

print(f"La categoría del postulante es: {categoria}")