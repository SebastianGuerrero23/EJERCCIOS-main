import os
os.system("cls")

donacion = int( input("Donacion : ") )

print(f"Centro Salud : {0.25 * donacion: .2f}")
print(f"Comedor infantil : {0.35 * donacion: .2f}")
print(f"Escuela infantil : {0.25 * donacion: .2f}")
print(f"Asilo : {0.15 * donacion : .2f}")