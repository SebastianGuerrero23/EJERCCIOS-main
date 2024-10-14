import os
os.system("cls")

base = float( input ("Ingreso la base del rectangulo: ") )
altura = float( input( "Ingreso la altura del rectangulo: ") )

area = base * altura 
perimetro = 2 * (base + altura)

print (f"Area del rectangulo = {area: .2f}")
print (f"Perimetro del rectangulo = {perimetro: .2f}")
