import os
os.system("cls")

def determinar_signo(numero):
    return "Positivo" * (numero > 0) + "Negativo" * (numero < 0) + "Cero" * (numero == 0)

# Ejemplo
numero = -5  

signo = determinar_signo(numero)
print(f"El número {numero} es {signo}.")