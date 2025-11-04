inversion=float(input("Introduzca la cantidad a invertir: "))
interes=float(input("Introduzca el porcentaje de interes anual: "))
anios=int(input("Introduzca el número de años: "))
anios=anios+1

for x in range(1,anios):
    print (inversion+(inversion*(interes/100)*x))
