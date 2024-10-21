import os
os.system("cls")

def interpretar_numero(numero):
    # Convertir el número a una cadena para acceder a cada cifra
    numero_str = str(numero)
    
    # Verificar que el número tenga exactamente 4 cifras
    if len(numero_str) != 4 or not numero_str.isdigit():
        return "Número inválido. Debe ser un entero positivo de 4 cifras."

    estado_civil = numero_str[0]  # Primera cifra
    edad = numero_str[1:3]         # Segunda y tercera cifras
    sexo = numero_str[3]            # Cuarta cifra
    
    # Interpretar el estado civil
    if estado_civil == '1':
        estado_civil_str = "Soltero"
    elif estado_civil == '2':
        estado_civil_str = "Casado"
    elif estado_civil == '3':
        estado_civil_str = "Divorciado"
    elif estado_civil == '4':
        estado_civil_str = "Viudo"
    else:
        estado_civil_str = "Estado civil no válido"
    
    # Obtener la edad
    edad_int = int(edad)
    
    # Interpretar el sexo
    if sexo == '1':
        sexo_str = "Masculino"
    elif sexo == '2':
        sexo_str = "Femenino"
    else:
        sexo_str = "Sexo no válido"

    return f"Estado Civil: {estado_civil_str}, Edad: {edad_int}, Sexo: {sexo_str}"

# Ejemplo de uso
numero_asignado = 2319  # Cambia este valor según el número asignado

resultado = interpretar_numero(numero_asignado)
print(resultado)
