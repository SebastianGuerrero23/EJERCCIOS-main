import os
os.system("cls")

def distribuir_donacion(monto_donacion):
    if monto_donacion >= 10000:
        centro_salud = monto_donacion * 0.30  # 30% al centro de salud
        comedor_ninos = monto_donacion * 0.50  # 50% al comedor de niños
    else:
        centro_salud = monto_donacion * 0.25  # 25% al centro de salud
        comedor_ninos = monto_donacion * 0.60  # 60% al comedor de niños
    
    # El resto que se invierte en la bolsa
    inversion_bolsa = monto_donacion - (centro_salud + comedor_ninos)
    
    return centro_salud, comedor_ninos, inversion_bolsa

# Ejemplo 
monto_donacion = 8000 

centro_salud, comedor_ninos, inversion_bolsa = distribuir_donacion(monto_donacion)

print(f"Monto destinado al centro de salud: $ {centro_salud:.2f}")
print(f"Monto destinado al comedor de niños: $ {comedor_ninos:.2f}")
print(f"Monto destinado a la inversión en la bolsa: $ {inversion_bolsa:.2f}")
