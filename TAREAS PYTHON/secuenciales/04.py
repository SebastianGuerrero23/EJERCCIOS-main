import os
os.system("cls")

# Entradas

pies = int( input("Ingrese la estatura en pies: ") )
pulgadas = int( input("Ingrese las pulgadas adicianles") )

# Factores de conversion
pies_a_metros = pies * 0.3048 # 1 pie = 0.3048 metros
pulgadas_a_metros = pulgadas * 0.0254 # 1 pulgada = 0.254 metros

# Calcular la estatura total en metros
estatura_metros = pies_a_metros + pulgadas_a_metros

# Salida
print (f"Estatura en metros = {estatura_metros:.2f}")