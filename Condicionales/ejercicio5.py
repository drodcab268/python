edad=int(input("Introduzca su edad: "))
ing=int(input("Inroduzca sus ingresos mensuales: "))

if edad > 16:
    if ing >= 1000:
        print("Usted debe tributar")
    else:
        print("Usted está exento de tributar")
else:
    print("Usted está exento de tributar")

