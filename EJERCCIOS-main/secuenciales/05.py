import os
os.system("cls")

capacidad_gb = float(input("Ingrese la capacidad del disco duro en gigabytes: "))

capacidad_mb = capacidad_gb * 1024  # Gigabytes a Megabytes
capacidad_kb = capacidad_mb * 1024   # Megabytes a Kilobytes
capacidad_bytes = capacidad_kb * 1024 # Kilobytes a Bytes

print(f"Capacidad en Megabytes: {capacidad_mb:.2f} MB")
print(f"Capacidad en Kilobytes: {capacidad_kb:.2f} KB")
print(f"Capacidad en Bytes: {capacidad_bytes:.2f} Bytes")