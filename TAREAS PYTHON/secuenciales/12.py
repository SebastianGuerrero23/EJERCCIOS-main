import os, math
os.system("cls")

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
     raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
     raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
     resultado = f"Las raíces son: {raiz1:.2f} y {raiz2:.2f}"

elif discriminante == 0:
     raiz = -b / (2*a)
     resultado = f"La raíz doble es: {raiz:.2f}"

else:
     parte_real = -b / (2*a)
     parte_imaginaria = math.sqrt(-discriminante) / (2*a)
     resultado = f"Las raíces son complejas: {parte_real:.2f} + {parte_imaginaria:.2f}i y {parte_real:.2f} - {parte_imaginaria:.2f}i"

print


