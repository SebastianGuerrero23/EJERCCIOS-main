import os
os.system("cls")

# Entradas
tramo_1_km = float( input("Tramo 1 en km: ") )
tramo_2_pies = float( input("Tramo 2 en pies: ") )
tramo_3_millas = float( input("Tramo 3 en millas: ") )

# Conversiones a metros 
total_metros = (tramo_1_km * 1000) + (tramo_2_pies / 3.2808) + (tramo_3_millas * 1609)

# Conversion a yardasç
total_yardas = total_metros * 1.09361

# Salida 
print (f"Total en metros = {total_metros:.2f}")
print (f"Total en yardas = {total_yardas:.2f}")

