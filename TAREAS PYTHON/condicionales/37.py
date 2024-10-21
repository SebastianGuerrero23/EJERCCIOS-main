import os
os.system("cls")

def determinar_resultados(votos_pamela, votos_carol, votos_fanny):
    total_votos = votos_pamela + votos_carol + votos_fanny
    if total_votos == 0:
        return "No hay votos emitidos."
    
    # Calcular la mitad de los votos más uno para ganar
    umbral_ganador = total_votos / 2 + 1

    # Verificar quién ganó o si hay empate
    if (votos_pamela >= umbral_ganador and 
        votos_carol < umbral_ganador and 
        votos_fanny < umbral_ganador):
        return "Ganadora: Pamela"
    elif (votos_carol >= umbral_ganador and 
          votos_pamela < umbral_ganador and 
          votos_fanny < umbral_ganador):
        return "Ganadora: Carol"
    elif (votos_fanny >= umbral_ganador and 
          votos_pamela < umbral_ganador and 
          votos_carol < umbral_ganador):
        return "Ganadora: Fanny"
    elif (votos_pamela == votos_carol and votos_pamela == votos_fanny):
        return "Empate entre los tres candidatos. Elección anulada."
    elif (votos_pamela == votos_carol and votos_pamela > votos_fanny):
        return "Empate entre Pamela y Carol. Segunda vuelta entre ellas."
    elif (votos_pamela == votos_fanny and votos_pamela > votos_carol):
        return "Empate entre Pamela y Fanny. Segunda vuelta entre ellas."
    elif (votos_carol == votos_fanny and votos_carol > votos_pamela):
        return "Empate entre Carol y Fanny. Segunda vuelta entre ellas."
    else:
        # Ordenar resultados
        resultados = [(votos_pamela, "Pamela"), (votos_carol, "Carol"), (votos_fanny, "Fanny")]
        resultados.sort(reverse=True, key=lambda x: x[0])
        
        puestos = []
        for i, (voto, nombre) in enumerate(resultados):
            puestos.append(f"{i + 1}° puesto: {nombre} con {voto} votos")
        
        return "\n".join(puestos)

# Ejemplo de uso
votos_pamela = int(input("Ingrese el número de votos para Pamela: "))
votos_carol = int(input("Ingrese el número de votos para Carol: "))
votos_fanny = int(input("Ingrese el número de votos para Fanny: "))

resultado = determinar_resultados(votos_pamela, votos_carol, votos_fanny)
print(resultado)
