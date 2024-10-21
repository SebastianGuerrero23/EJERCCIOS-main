import os
os.system("cls")

def son_consecutivas(numero):
    
    # Convertir el número a una lista de dígitos
    cifras = [int(d) for d in str(numero)]
    
    # Verificar si tiene exactamente 3 cifras
    if len(cifras) == 3:
        # Comprobar si están en orden ascendente o descendente
        es_ascendente = (cifras[0] + 1 == cifras[1] and cifras[1] + 1 == cifras[2])
        es_descendente = (cifras[0] - 1 == cifras[1] and cifras[1] - 1 == cifras[2])
        
        if es_ascendente:
            return "Las cifras son consecutivas en orden ascendente."
        elif es_descendente:
            return "Las cifras son consecutivas en orden descendente."
        else:
            return "Las cifras no son consecutivas."
    else:
        return "El número no tiene exactamente tres cifras."

# Ejemplo
numero = 321  

resultado = son_consecutivas(numero)
print(resultado)